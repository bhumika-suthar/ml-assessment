Welcome to the Machine Learning and Web Scraping Project! This repository contains a collection of Python scripts and utilities designed to perform machine learning tasks and web scraping, with support for ChromeDriver automation.
Project Structure
* llm_filter.py: Contains logic for filtering or processing large language model outputs.
* main.py: The primary entry point for running the project.
* model.py: Defines the machine learning models or related classes used in the project.
* requirements.txt: Lists the Python dependencies required to run the project.
* scrapers.py: Includes web scraping utilities, likely utilizing ChromeDriver for browser automation.
* utils.py: Contains helper functions and utilities used across the project.
* init.txt: Configuration file for project settings, such as Chrome version, debug mode, and file paths.
Installation
1. Clone the repository: git clone https://github.com/bhumika-suthar/ml-assessment cd machine-learning-web-scraping
2. Install the required dependencies: pip install -r requirements.txt
3. Ensure you have a compatible version of Chrome and ChromeDriver installed. Starting with Chrome version M115, the ChromeDriver release process is integrated with Chrome. Check the Chrome for Testing (CfT) availability dashboard (https://googlechromelabs.github.io/chrome-for-testing/) for the latest releases. For automated version matching, use the CfT JSON endpoints as described in the assessment PDF.
o If manual version selection is needed, match your Chrome binary's MAJOR.MINOR.BUILD version with a compatible ChromeDriver version using the latest-patch-versions-per-build JSON endpoint.
o Configure the Chrome version in init.txt under the [SETTINGS] section (e.g., chrome_version = auto for the latest version).
4. Set up the init.txt file with your project-specific settings (see the Configuration section below).
Configuration
The init.txt file contains project settings. Edit it to customize your setup:
Initialization Configuration for Machine Learning and Web Scraping Project
Date: March 18, 2025
[SETTINGS] project_name = Machine Learning and Web Scraping chrome_version = auto # Set to 'auto' for latest CfT version or specify MAJOR.MINOR.BUILD debug_mode = False
[PATHS] data_dir = ./data log_file = ./logs/project.log
[DEFAULTS] model_type = default_model scraper_timeout = 30 # seconds
Use a library like configparser in Python to read these settings in your scripts. Example: import configparser
def load_config(): config = configparser.ConfigParser() config.read('init.txt') return config
config = load_config() chrome_version = config['SETTINGS']['chrome_version'] print(f"Using Chrome Version: {chrome_version}")
Usage
1. Run the main script to start the project: python main.py
2. Configure the scraping or model training parameters in main.py, init.txt, or the respective module files as needed.
Features
* Machine Learning: Utilize custom models defined in model.py and filtered outputs via llm_filter.py.
* Web Scraping: Leverage scrapers.py to extract data, with support for ChromeDriver automation.
* Utilities: General-purpose functions in utils.py to streamline development.
* Configuration: Flexible settings management via init.txt.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure to update the requirements.txt file if new dependencies are added and modify init.txt if new configurations are introduced.
License
This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the LICENSE file for details.
Contact
For questions or support, please open an issue in the repository or contact the project maintainer.

