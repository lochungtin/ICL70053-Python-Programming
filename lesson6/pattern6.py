length = 9

for i in range(-4, 5):
    absVal = abs(i)

    pattern = ""
    for j in range((9 - absVal * 2)):
        pattern += ". " if j % 2 else "* "

    print("  " * absVal + pattern)
