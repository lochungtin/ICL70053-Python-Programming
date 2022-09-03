def load_indexed_employees(filename):
    employees = {}
    for line in open(filename):
        [id, name, age, nationality] = line.strip().split(",")
        employees[id] = {"id": id, "name": name, "age": age, "nationality": nationality}

    return employees


def group_by(employees, criterion):
    rt = {}
    for (id, data) in employees.items():
        grouping = data[criterion]
        if grouping not in rt:
            rt[grouping] = []

        rt[grouping].append(id)

    return rt


employee_dict = load_indexed_employees(
    "lesson7/employee_mini_project/employee_details.txt"
)
print(len(employee_dict))

employee_ids = list(employee_dict)
print(employee_ids)
print(employee_dict[employee_ids[0]])

group_by_nationality = group_by(employee_dict, "nationality")
print(group_by_nationality)
