import math

n = float(input("Please enter a number: "))
estimate = 0

increment = 1
margin = 0.00001

while abs(estimate**2 - n) > margin:
    while estimate**2 < n:
        estimate += increment

    estimate -= increment
    increment /= 10

gold_reference = math.sqrt(n)
if abs(estimate - gold_reference) < 0.00001:
    print("Correct. estimate: {}, gold reference: {}".format(estimate, gold_reference))
else:
    print(
        f"Incorrect. Program output is {estimate}, but I am expecting {gold_reference}."
    )
