primes = []

n = int(input("Please enter an integer: "))
sweeper = 2

while sweeper < n:
    is_prime = True
    for prime in primes:
        is_prime *= sweeper % prime != 0

    if is_prime:
        primes.append(sweeper)

    sweeper += 1

for prime in primes:
    print(prime)
