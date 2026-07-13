from resume_analyzer import analyze_resume
from application_generator import generate_application
from job_loader import load_jobs
from job_parser import extract_job_info
from job_parser_utils import parse_job_info
from tracker.application_tracker import add_application



# -------------------------
# Load Resume
# -------------------------

with open(
    "resume/resume.txt",
    "r",
    encoding="utf-8"
) as file:

    resume = file.read()



# -------------------------
# Load Jobs
# -------------------------

jobs = load_jobs()


print("\nJobs Found:")
print(len(jobs))


print("\n==============================")
print("JOB ANALYSIS RESULTS")
print("==============================\n")



results = []



# -------------------------
# Process Jobs
# -------------------------

for job in jobs:

    print("\nProcessing:")
    print(job["filename"])


    job_description = job["description"]



    # -------------------------
    # Parse Job Information
    # -------------------------

    job_response = extract_job_info(
        job_description
    )


    job_info = parse_job_info(
        job_response
    )


    print("\nJob Information:")
    print(job_info)



    # -------------------------
    # Resume Analysis
    # -------------------------

    analysis = analyze_resume(
        resume,
        job_description
    )


    print("\nResume Analysis:")
    print(analysis)



    # -------------------------
    # Generate Application
    # -------------------------

    package = generate_application(
        resume,
        job_description
    )


    print("\nApplication Package Generated")



    # -------------------------
    # Save Result
    # -------------------------

    results.append(
        {
            "job": job_info,
            "analysis": analysis
        }
    )



    # -------------------------
    # Track Application
    # -------------------------

    add_application(
        company=job_info["company"],
        role=job_info["role"],
        status="Review",
        match_score="Pending",
        notes="Generated application package"
    )



# -------------------------
# Complete
# -------------------------

print("\n==============================")
print("PROCESS COMPLETE")
print("==============================")


print(
    f"\nProcessed {len(results)} jobs."
)