def load_verbs_from_file(filename):
    return [line.strip() for line in open(filename)]


verbs = load_verbs_from_file("lesson6/verbs2.txt")

ing = [verb + "ing" for verb in verbs]
ed = [verb + "ed" for verb in verbs]

for verb in ing + ed:
    print(verb)
