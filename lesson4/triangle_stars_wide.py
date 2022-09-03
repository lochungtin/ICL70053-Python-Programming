rows = int(input("Enter an integer: "))

counter = 0
while counter < rows:
    counter += 1
    print("*" * (2 * counter - 1))
