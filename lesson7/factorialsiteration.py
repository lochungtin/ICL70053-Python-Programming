def factorial(num):
    prod = 1
    for i in range(1, num + 1):
        prod *= i

    return prod


print(factorial(5))
