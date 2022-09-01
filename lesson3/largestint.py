num1 = int(input("Please enter the first integer: "))
num2 = int(input("Please enter the second integer: "))
num3 = int(input("Please enter the third integer: "))

if num1 > num2:
    larger = num1
else:
    larger = num2

if num3 > larger:
    print(num3)
else:
    print(larger)
