num = int(input("Please enter an integer: "))
sweeper = 2
is_prime = True

while sweeper < num:
    if num % sweeper == 0:
        is_prime = False
        break

    sweeper += 1

if is_prime:
    print("{} is a prime number".format(num))
else:
    print("{} is not a prime number".format(num))
