from random import randint

# settings
upperbound = 50
attempts = 10

# correctness settings
cool_margin = 15
warm_margin = 8
hot_margin = 3

# data
guess = -1
target = randint(0, upperbound)

# algorithm
while guess != target and attempts >= 0:
    attempts -= 1
    guess = int(input("Enter your guess: "))

    diff = abs(guess - target)
    if diff == 0:
        print("Your guess is correct!")
    elif diff < hot_margin:
        print("Your guess is hot.")
    elif diff < warm_margin:
        print("Your guess is warm.")
    elif diff < cool_margin:
        print("Your guess is cool.")
    else:
        print("Your guess is cold.")

if guess != target and attempts < 0:
    print("You ran out of attempts.")
    print("The correct number is", target)
