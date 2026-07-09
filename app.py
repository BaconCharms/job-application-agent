from resume_analyzer import analyze_resume
from application_generator import generate_application


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



# Resume Analysis

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



# Application Generation

application = generate_application(
    resume,
    job_description
)


print("\n\nApplication Package:\n")
print(application)


with open(
    "output/application_package.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(application)