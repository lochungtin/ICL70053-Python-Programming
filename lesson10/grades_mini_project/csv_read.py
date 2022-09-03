import csv

with open("lesson10/grades_mini_project/students.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=",", skipinitialspace=True)
    header_row = next(reader)

    for row in reader:
        print("{} {}: {} ({})".format(row[1], row[0], row[7], row[8]))
