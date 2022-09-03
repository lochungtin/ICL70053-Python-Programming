def compute_min_divisible(numbers, divisor):
    divisible = [number for number in numbers if number % divisor == 0]
    if len(divisible):
        return min(divisible)

    return None


print(compute_min_divisible([34, 5, 10, 19, 28, 74], 3))
