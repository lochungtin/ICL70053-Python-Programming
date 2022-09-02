def is_prime_number(num):
    sweeper = 2
    while sweeper < num:
        if num % sweeper == 0:
            return False

        sweeper += 1

    return True


def read_integer():
    return int(input("Please enter an integer: "))


num = read_integer()
if is_prime_number():
    print("{} is a prime number".format(num))
else:
    print("{} is not a prime number".format(num))
