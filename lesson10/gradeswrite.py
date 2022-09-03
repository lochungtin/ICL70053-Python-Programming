import csv

with open("lesson10/students.csv") as csv_file:
    reader = csv.DictReader(csv_file, skipinitialspace=True)

    data = [
        {
            "First name": row["First name"],
            "Last name": row["Last name"],
            "Final": row["Final"],
            "Grade": row["Grade"],
        }
        for row in reader
    ]

headers = ["First name", "Last name", "Final", "Grade"]
with open("lesson10/students_out.csv", "w+") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers, delimiter=",")
    writer.writeheader()
    writer.writerows(data)
