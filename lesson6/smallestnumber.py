user_input = None
numbers = []

while True:
    user_input = input("Please enter an integer: ")
    if user_input == "q":
        break
    else:
        numbers.append(int(user_input))

smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number

print(smallest)
