import math

n = float(input("Please enter a number: "))
estimate = 1
prev = 0

margin = 0.00001

while True:
    prev = estimate
    estimate = (estimate + (n / estimate)) / 2
    if abs(prev - estimate) < margin:
        break

gold_reference = math.sqrt(n)
if abs(estimate - gold_reference) < 0.00001:
    print("Correct. estimate: {}, gold reference: {}".format(estimate, gold_reference))
else:
    print(
        f"Incorrect. Program output is {estimate}, but I am expecting {gold_reference}."
    )
