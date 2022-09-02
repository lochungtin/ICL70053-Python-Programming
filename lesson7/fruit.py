fruits = ["apples", "oranges", "bananas", "pineapples", "mangoes"]

try:
    inVal = input("Enter an integer: ")
    index = int(inVal)

    fruit = fruits[index]
    print(f"You love {fruit}!")

except ValueError:
    print("Input {} is not a number".format(inVal))

except IndexError:
    print("No fruit at index {}".format(index))
