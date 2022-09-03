def load_transations(filename):
    rt = {}
    with open(filename) as textfile:
        all_lines = textfile.readlines()
        for line in all_lines:
            dataline = line.strip().split("\t")
            rt[dataline[0]] = dataline[1:]

    return rt


def translate(sentence, translation_dict):
    return " ".join([translation_dict[word][0] for word in sentence.split(" ")])


translation_dict = load_transations("lesson7/french.txt")
translation = translate("a boy with a ball in the park", translation_dict)
print(translation)
