def convert_to_lowercase(filename):
    outfilename = filename[:-4] + "_lower.txt"
    with open(filename) as infile, open(outfilename, "w+") as outfile:
        while True:
            line = infile.readline()

            if line == "":
                break
            if line == "\n":
                continue

            for word in line.strip().split(" "):
                outfile.write(word.lower() + "\n")

    return outfilename


outfilename = convert_to_lowercase("lesson8/hamlet.txt")
print(outfilename)
