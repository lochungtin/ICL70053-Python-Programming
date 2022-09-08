import re


def loadAccuracy(filename):
    with open(filename, "r") as infile:
        for line in infile.readlines():
            match = re.match("(\s)*accuracy(\s)*(?P<value>\d.\d+)", line)
            if match != None:
                return match.group("value")


accuracy1 = loadAccuracy("adv_lesson1/ch1/classification1.txt")
accuracy2 = loadAccuracy("adv_lesson1/ch1/classification2.txt")

print(accuracy1, accuracy2)
