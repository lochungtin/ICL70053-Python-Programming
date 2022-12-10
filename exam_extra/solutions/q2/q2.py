def filter_e(string):
    new_string = []
    words = string.split()
    for word in words:
        if "e" not in word:
            new_string.append(word)
    return " ".join(new_string)


# Alternative solution
def filter_e_v2(string):
    words = string.split()
    new_string = [word for word in words if "e" not in word]
    return " ".join(new_string)


# Alternative solution
def filter_e_v3(string):
    words = string.split()
    new_string = filter(lambda w: "e" not in w, words)
    return " ".join(new_string)
