def increment_list(numbers, step=1):
    return [number + step for number in numbers]


numbers = [1, 2, 3, 4]
incremented_numbers = increment_list(numbers)
print(incremented_numbers)
