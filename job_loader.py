import os


JOBS_FOLDER = "jobs"


def load_jobs():

    jobs = []

    for filename in os.listdir(JOBS_FOLDER):

        if filename.endswith(".txt"):

            filepath = os.path.join(
                JOBS_FOLDER,
                filename
            )

            with open(
                filepath,
                "r",
                encoding="utf-8"
            ) as file:

                jobs.append(
                    {
                        "filename": filename,
                        "description": file.read()
                    }
                )

    return jobs