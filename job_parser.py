from agent.agent import ask_agent


def extract_job_info(job_description):

    prompt = f"""
Extract the following information from this job description.

Return ONLY valid Python dictionary format:

{{
"company": "",
"role": "",
"location": ""
}}

JOB DESCRIPTION:

{job_description}
"""

    response = ask_agent(prompt)

    return response