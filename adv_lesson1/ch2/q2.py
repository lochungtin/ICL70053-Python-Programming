import re


def loadTotal(filename):
    with open(filename, "r") as infile:
        for line in infile.readlines():
            match = re.match("^(\s)+TOTAL(\s)+£(?P<value>.+)$", line)

            if match != None:
                return match.group("value")


print(loadTotal("adv_lesson1/ch2/receipt.txt"))
