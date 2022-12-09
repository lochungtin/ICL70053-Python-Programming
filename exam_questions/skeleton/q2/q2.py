# def filter_e(string):
#     rt = []
#     for word in string.split(" "):
#         if "e" not in word:
#             rt.append(word)

#     return " ".join(rt)


def filter_e(string):
    return " ".join(filter(lambda x: "e" not in x, string.split(" ")))
