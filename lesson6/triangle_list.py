from re import L


def generate_triangle_list(length):
    return [list(range(1, i + 1)) for i in range(1, length + 1)]


print(generate_triangle_list(6))
