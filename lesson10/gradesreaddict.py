import csv

with open("lesson10/students.csv") as csv_file:
    reader = csv.DictReader(csv_file, skipinitialspace=True)

    for row in reader:
        print(
            "{} {}: {} ({})".format(
                row["First name"], row["Last name"], row["Final"], row["Grade"]
            )
        )
