from job_loader import load_jobs


jobs = load_jobs()

print()

print("Jobs Found:")

print()

for job in jobs:

    print(job["filename"])

    print("-" * 30)

    print(job["description"])

    print()