from agent import ask_agent


with open(
    "jobs/sample_job.txt",
    "r",
    encoding="utf-8"
) as file:

    job_description = file.read()


prompt = f"""
You are an expert career coach and recruiter.

Analyze this job description.

Provide:

1. Required skills
2. Important resume keywords
3. What experiences I should highlight
4. Interview preparation topics
5. Overall fit assessment

Job Description:

{job_description}
"""


answer = ask_agent(prompt)


print("\nAI Agent Response:\n")
print(answer)


with open(
    "output/job_analysis.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(answer)

