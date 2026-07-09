from agent import ask_agent


def analyze_resume(resume, job_description):

    prompt = f"""
You are an expert recruiter and resume strategist.

Compare the candidate resume against the job description.

Provide:

1. Overall match score out of 100
2. Strong matching qualifications
3. Missing skills or experience
4. Resume improvements
5. Specific bullet points to emphasize
6. Interview talking points


CANDIDATE RESUME:

{resume}


JOB DESCRIPTION:

{job_description}

"""

    response = ask_agent(prompt)

    return response