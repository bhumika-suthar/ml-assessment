from pydantic import BaseModel

class JobSearchRequest(BaseModel):
    position: str
    experience: str
    salary: str
    jobNature: str
    location: str
    skills: str

class JobResponse(BaseModel):
    job_title: str
    company: str
    experience: str
    jobNature: str
    location: str
    salary: str
    apply_link: str