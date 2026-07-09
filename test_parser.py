from job_parser import extract_job_info


with open(
    "jobs/sample_job.txt",
    "r",
    encoding="utf-8"
) as file:

    job = file.read()


info = extract_job_info(job)

print(info)