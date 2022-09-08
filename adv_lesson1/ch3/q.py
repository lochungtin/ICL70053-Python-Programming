import re


def loadEmails(filename):
    rt = []
    with open(filename, "r") as infile:
        for line in infile.readlines():
            if line.startswith("To: "):
                splts = re.split(", ", line[4:])

                for splt in splts:
                    print(splt)
                    match = re.match('"(?P<name>[A-Za-z\s]+)" <(?P<email>.+)>', splt)
                    rt.append((match.group("name"), match.group("email")))

    return rt


for (name, email) in loadEmails("adv_lesson1/ch3/email.txt"):
    print("{}, {}".format(name, email))
