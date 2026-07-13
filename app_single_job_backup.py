from resume_analyzer import analyze_resume
from application_generator import generate_application
from tracker.application_tracker import add_application
from job_parser import extract_job_info
from job_parser_utils import parse_job_info
from score_parser import extract_match_score


# Load Resume

with open(
    "resume/resume.txt",
    "r",
    encoding="utf-8"
) as file:

    resume = file.read()



# Load Job Description

with open(
    "jobs/sample_job.txt",
    "r",
    encoding="utf-8"
) as file:

    job_description = file.read()



# Extract Job Information

job_response = extract_job_info(
    job_description
)

job_info = parse_job_info(
    job_response
)


print("\nJob Information:\n")
print(job_info)



# Analyze Resume Against Job

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



# Generate Application Package

application = generate_application(
    resume,
    job_description
)

match_score = extract_match_score(
    analysis
)

print("\nApplication Package:\n")
print(application)



with open(
    "output/application_package.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(application)



# Save Application To Tracker

add_application(
    job_info["company"],
    job_info["role"],
    match_score,
    "Generated resume analysis and application package"
)