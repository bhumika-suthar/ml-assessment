import logging
from typing import Dict, Any

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_request(request_data: Dict[str, Any]):
    """
    Log the incoming request data.
    """
    logger.info(f"Incoming request data: {request_data}")

def log_error(error: Exception):
    """
    Log an error.
    """
    logger.error(f"An error occurred: {error}")

def validate_input(request_data: Dict[str, Any]) -> bool:
    """
    Validate the input data for the job search request.
    """
    required_fields = ["position", "experience", "salary", "jobNature", "location", "skills"]
    for field in required_fields:
        if field not in request_data:
            logger.error(f"Missing required field: {field}")
            return False
    return True

def format_response(jobs: list) -> Dict[str, Any]:
    """
    Format the response data into a structured JSON format.
    """
    return {"relevant_jobs": jobs}

def handle_error(error: Exception) -> Dict[str, str]:
    """
    Handle errors and return a standardized error response.
    """
    log_error(error)
    return {"error": str(error)}