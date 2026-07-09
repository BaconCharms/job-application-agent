from resume_analyzer import analyze_resume


with open(
    "resume/resume.txt",
    "r",
    encoding="utf-8"
) as file:

    resume = file.read()



with open(
    "jobs/sample_job.txt",
    "r",
    encoding="utf-8"
) as file:

    job_description = file.read()



analysis = analyze_resume(
    resume,
    job_description
)



print("\nResume Analysis:\n")
print(analysis)


with open(
    "output/resume_analysis.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(analysis)