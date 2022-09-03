minute = 5

while minute > 0:
    print(minute)
    second = 60
    while second > 0:
        if second % 10 == 0:
            print(second)
        second -= 1

    if minute == 2:
        print("Almost there!")

    minute -= 1

print("Time's up!!")
