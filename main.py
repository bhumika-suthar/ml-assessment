from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scrapers import scrape_linkedin_jobs, scrape_indeed_jobs  # Ensure this import is correct
from utils import log_request, validate_input, format_response, handle_error
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

class JobSearchRequest(BaseModel):
    position: str
    experience: str
    salary: str
    jobNature: str
    location: str
    skills: str

@app.post("/search-jobs")
def search_jobs(request: JobSearchRequest):
    try:
        # Log the incoming request
        log_request(request.dict())

        # Validate the input
        if not validate_input(request.dict()):
            raise HTTPException(status_code=400, detail="Invalid input data")

        # Scrape jobs from LinkedIn and Indeed
        linkedin_jobs = scrape_linkedin_jobs(request.position, request.location)
        indeed_jobs = scrape_indeed_jobs(request.position, request.location)  # Ensure this function is defined

        # Combine all jobs
        all_jobs = linkedin_jobs + indeed_jobs

        # Format the response
        return format_response(all_jobs)
    except Exception as e:
        # Handle errors
        error_response = handle_error(e)
        raise HTTPException(status_code=500, detail=error_response["error"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)