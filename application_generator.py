from agent.agent import ask_agent


def generate_application(resume, job_description):

    prompt = f"""
You are an expert resume writer and career coach.

Using the candidate resume and job description below,
create a customized job application package.

Candidate Resume:

{resume}


Job Description:

{job_description}


Provide:

1. Customized resume bullet points
2. Professional summary tailored to this role
3. Cover letter draft
4. Interview talking points
5. Key skills to emphasize
"""

    response = ask_agent(prompt)

    return response