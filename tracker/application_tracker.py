import csv
from datetime import date


APPLICATION_FILE = "data/applications.csv"



def application_exists(company, role):

    try:
        with open(
            APPLICATION_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
                if (
                    row["company"] == company
                    and row["role"] == role
                ):
                    return True

    except FileNotFoundError:
        return False

    return False



def add_application(
    company,
    role,
    match_score,
    notes=""
):

    if application_exists(company, role):
        print("Application already exists in tracker.")
        return


    with open(
        APPLICATION_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            company,
            role,
            date.today(),
            "Applied",
            match_score,
            notes
        ])

    print("Application added to tracker.")



def view_applications():

    with open(
        APPLICATION_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.reader(file)

        for row in reader:
            print(row)



def get_applications():

    applications = []

    with open(
        APPLICATION_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            applications.append(row)

    return applications