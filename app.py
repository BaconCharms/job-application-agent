from resume_analyzer import analyze_resume
from application_generator import generate_application
from job_loader import load_jobs
from job_parser import extract_job_info
from job_parser_utils import parse_job_info
from tracker.application_tracker import add_application
from job_qualifier import qualify_job



# ==============================
# Load Resume
# ==============================

with open(
    "resume/resume.txt",
    "r",
    encoding="utf-8"
) as file:

    resume = file.read()



# ==============================
# Load Jobs
# ==============================

jobs = load_jobs()


print("\nJobs Found:")
print(len(jobs))


print("\n==============================")
print("JOB ANALYSIS RESULTS")
print("==============================\n")



results = []



# ==============================
# Process Each Job
# ==============================

for job in jobs:


    print("\nProcessing:")
    print(job["filename"])


    job_description = job["description"]



    # ------------------------------
    # Extract Job Information
    # ------------------------------

    job_response = extract_job_info(
        job_description
    )


    job_info = parse_job_info(
        job_response
    )


    print("\nJob Information:")
    print(job_info)



    # ------------------------------
    # Analyze Resume Match
    # ------------------------------

    analysis = analyze_resume(
        resume,
        job_description
    )


    print("\nResume Analysis:")
    print(analysis)



    # ------------------------------
    # Job Qualification
    # ------------------------------

    decision = qualify_job(
        job_info,
        analysis
    )


    print("\nJob Qualification:")
    print(decision)



    # ------------------------------
    # Skip Poor Matches
    # ------------------------------

    if decision["decision"] == "REJECT":

        print(
            "Skipping application generation."
        )

        continue



    # ------------------------------
    # Generate Application Package
    # ------------------------------

    package = generate_application(
        resume,
        job_description
    )


    print(
        "\nApplication Package Generated"
    )



    # ------------------------------
    # Store Results
    # ------------------------------

    results.append(
        {
            "job": job_info,
            "analysis": analysis,
            "decision": decision
        }
    )



    # ------------------------------
    # Track Application
    # ------------------------------

    add_application(
        company=job_info["company"],
        role=job_info["role"],
        status="Review",
        match_score=decision["match_score"],
        notes=decision["reason"]
    )



# ==============================
# Completion
# ==============================

print("\n==============================")
print("PROCESS COMPLETE")
print("==============================")


print(
    f"\nProcessed {len(results)} jobs."
)