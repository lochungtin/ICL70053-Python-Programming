def load_database(filename):
    database = {}
    for line in open(filename):
        [key, value] = line.strip().split(",")
        database[key] = value

    return database


def query_database(database, queries):
    return [database.get(query, None) for query in queries]


employee_dict = load_database("lesson7/employee_mini_project/employees.txt")

queries = ["14817102", "12345678", "61098940"]
names = query_database(employee_dict, queries)

print(names)
