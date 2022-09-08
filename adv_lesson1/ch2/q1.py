import re


def loadItems(filename):
    rt = []
    with open(filename, "r") as infile:
        for line in infile.readlines():
            match = re.match(
                "^(?P<name>[A-Z0-9\s]+[A-Z0-9]+)(\s)+(\d)+(\s)+£(?P<value>\d+.\d+)",
                line,
            )

            if match != None:
                rt.append((match.group("name"), match.group("value")))

    return rt


total = 0
for (item, value) in loadItems("adv_lesson1/ch2/receipt.txt"):
    print(item, value)
    total += float(value)

print(total)
