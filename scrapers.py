from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

def scrape_linkedin_jobs(position, location):
    # Specify the path to ChromeDriver
    chrome_driver_path = "C:\\path\\to\\chromedriver.exe"  # Update this path
    service = Service(chrome_driver_path)

    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    options.add_argument("--disable-gpu")  # Disable GPU acceleration
    options.add_argument("--no-sandbox")  # Disable sandboxing

    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=service, options=options)

    # Open LinkedIn Jobs page
    driver.get("https://www.linkedin.com/jobs/")

    # Wait for the page to load
    time.sleep(5)

    # Enter job position and location
    search_position = driver.find_element(By.NAME, "keywords")
    search_position.send_keys(position)
    search_location = driver.find_element(By.NAME, "location")
    search_location.send_keys(location)
    search_location.send_keys(Keys.RETURN)

    # Wait for results to load
    time.sleep(5)

    # Scrape job listings
    jobs = []
    job_listings = driver.find_elements(By.CLASS_NAME, "base-card")  # Update class name as needed
    for job in job_listings:
        title = job.find_element(By.CLASS_NAME, "base-search-card__title").text
        company = job.find_element(By.CLASS_NAME, "base-search-card__subtitle").text
        location = job.find_element(By.CLASS_NAME, "job-search-card__location").text
        link = job.find_element(By.TAG_NAME, "a").get_attribute("href")
        jobs.append({
            "job_title": title,
            "company": company,
            "location": location,
            "apply_link": link
        })

    # Close the browser
    driver.quit()

    return jobs

def scrape_indeed_jobs(position, location):
    # Construct the URL
    url = f"https://www.indeed.com/jobs?q={position}&l={location}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Send a GET request
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Scrape job listings
    jobs = []
    job_listings = soup.find_all("div", class_="job_seen_beacon")  # Update class name as needed
    for job in job_listings:
        title = job.find("h2", class_="jobTitle").text.strip()
        company = job.find("span", class_="companyName").text.strip()
        location = job.find("div", class_="companyLocation").text.strip()
        link = "https://www.indeed.com" + job.find("a")["href"]
        jobs.append({
            "job_title": title,
            "company": company,
            "location": location,
            "apply_link": link
        })

    return jobs