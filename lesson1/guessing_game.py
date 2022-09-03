from random import randint

# settings
upperbound = 50
attempts = 10

# correctness settings
margins = [0, 3, 7, 15, upperbound]
prompts = ["correct!", "hot.", "warm.", "cold", "cool."]

# data
guess = -1
target = randint(0, upperbound)

# algorithm
while guess != target and attempts >= 0:
    attempts -= 1
    guess = int(input("Enter your guess: "))
    for i in range(5):
        if abs(guess - target) <= margins[i]:
            print("Your guess is {}".format(prompts[i]))
            break

if guess != target and attempts < 0:
    print("You ran out of attempts.")
    print("The correct number is", target)
