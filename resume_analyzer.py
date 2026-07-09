from agent.agent import ask_agent


def analyze_resume(resume, job_description):

    prompt = f"""
Analyze the following resume against the following job description.

Resume:
{resume}

Job Description:
{job_description}

Provide:
1. Match score
2. Strengths
3. Weaknesses
4. Resume improvements
5. Interview talking points
"""

    response = ask_agent(prompt)

    return response