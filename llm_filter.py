import openai
import os

# Load OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def filter_jobs(jobs, user_criteria):
    relevant_jobs = []
    for job in jobs:
        prompt = f"Job Description: {job['description']}\nUser Criteria: {user_criteria}\nIs this job relevant? (yes/no):"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=10
        )
        if "yes" in response.choices[0].text.lower():
            relevant_jobs.append(job)
    return relevant_jobs