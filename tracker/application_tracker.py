import csv
import os
from datetime import date


APPLICATION_FILE = "data/applications.csv"


def application_exists(company, role):

    if not os.path.exists(APPLICATION_FILE):
        return False

    with open(
        APPLICATION_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            if (
                 row["company"].lower().strip() == company.lower().strip()
                and row["role"].lower().strip() == role.lower().strip()
            ):
                return True

    return False



def add_application(
    company,
    role,
    status,
    match_score,
    notes=""
):

    if application_exists(company, role):
        print("Application already exists in tracker.")
        return


    file_exists = os.path.exists(APPLICATION_FILE)


    with open(
        APPLICATION_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)


        if not file_exists:
            writer.writerow([
                "company",
                "role",
                "date_applied",
                "status",
                "match_score",
                "notes"
            ])


        writer.writerow([
            company,
            role,
            date.today(),
            status,
            match_score,
            notes
        ])


    print("Application added to tracker.")



def view_applications():

    if not os.path.exists(APPLICATION_FILE):
        print("No applications found.")
        return


    with open(
        APPLICATION_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            print(row)



def get_applications():

    applications = []


    if not os.path.exists(APPLICATION_FILE):
        return applications


    with open(
        APPLICATION_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            applications.append(row)


    return applications

def update_application_status(
    company,
    role,
    new_status
):

    if not os.path.exists(APPLICATION_FILE):
        return False


    applications = []


    with open(
        APPLICATION_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            if (
                row["company"].lower().strip() == company.lower().strip()
                and row["role"].lower().strip() == role.lower().strip()
            ):

                row["status"] = new_status

            applications.append(row)



    with open(
        APPLICATION_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "company",
                "role",
                "date_applied",
                "status",
                "match_score",
                "notes"
            ]
        )

        writer.writeheader()

        writer.writerows(applications)


    return True