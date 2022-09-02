try:
    with open("nosuchfile.txt") as textfile:
        for line in textfile:
            print(line)
except FileNotFoundError:
    print("No such file exists")
finally:
    print("I have an important message!")
