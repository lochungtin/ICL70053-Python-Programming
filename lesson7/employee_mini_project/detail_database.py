def load_employees(filename):
    employees = []
    for line in open(filename):
        [id, name, age, nationality] = line.strip().split(",")
        employees.append(
            {"id": id, "name": name, "age": age, "nationality": nationality}
        )

    return employees


def filter_employees(employees, criterion):
    rt = []

    for employee in employees:
        if employee[criterion[0]] == criterion[1]:
            rt.append(employee)

    return rt


employees = load_employees("lesson7/employee_mini_project/employee_details.txt")

criterion = ("nationality", "portugal")
filtered_employees = filter_employees(employees, criterion)

print(filtered_employees)
