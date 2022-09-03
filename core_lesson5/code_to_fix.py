def read_integer():
    return int(input("Please enter an integer: "))


def is_divisible_by(number, divisor):
    return number % divisor == 0


def is_prime_number(number):
    if number <= 1:
        return False

    divisor = 2
    while divisor < number:
        if is_divisible_by(number, divisor):
            return False
        else:
            divisor += 1
    return True


def get_prime_number_list(n):
    prime_number_list = []

    current_number = 2
    while len(prime_number_list) < n:
        if is_prime_number(current_number):
            prime_number_list.append(current_number)

        current_number += 1

    return prime_number_list


def sum_prime_number_list(prime_number_list):
    total = 0
    for number in prime_number_list:
        total += number

    return total


def sum_first_n_prime_numbers(n):
    prime_number_list = get_prime_number_list(n)
    total = sum_prime_number_list(prime_number_list)
    return total


n = read_integer()
total = sum_first_n_prime_numbers(n)
print(total)
