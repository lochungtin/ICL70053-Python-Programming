year = int(input("Please enter year: "))

false_text = "Not a leap year"
true_text = "Leap year"

if year % 400 == 0:
    print(true_text)
elif year % 4 == 0 and year % 100:
    print(true_text)
else:
    print(false_text)
