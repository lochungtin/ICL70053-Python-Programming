import re


def loadF1(filename):
    rt = []
    with open(filename, "r") as infile:
        for line in infile.readlines():
            match = re.match(
                "(\s)*\d(\s)+(?:\d.\d+)(\s)+(?:\d.\d+)(\s)+(?P<value>\d.\d+)",
                line,
            )
            if match != None:
                rt.append(match.group("value"))

    return rt


for cls, val in enumerate(loadF1("adv_lesson1/ch1/classification1.txt")):
    print("f1-score for class {} = {}".format(cls, val))

for cls, val in enumerate(loadF1("adv_lesson1/ch1/classification2.txt")):
    print("f1-score for class {} = {}".format(cls, val))
