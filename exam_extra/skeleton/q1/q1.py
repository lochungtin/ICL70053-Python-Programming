# def longest_word(words):
#     rt = ("", -1)
#     for word in words:
#         l = len(word)
#         if l > rt[1]:
#             rt = (word, l)
#     return rt


def longest_word(words):
    return max(map(lambda x: (x, len(x)), words), key=lambda x: x[1])
