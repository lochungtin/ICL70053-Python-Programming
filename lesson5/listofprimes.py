primes = []


def is_prime_number(num):
    global primes
    for prime in primes:
        if num % prime == 0:
            return False
    return True


def find_primes(limit):
    global primes
    sweeper = 2
    while sweeper < limit:
        if is_prime_number(sweeper):
            primes.append(sweeper)
            print(sweeper)

        sweeper += 1


def read_integer():
    return int(input("Please enter an integer: "))


num = read_integer()
find_primes(num)
