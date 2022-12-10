# def odd_even_swap(word):
#     l = list(word)
#     for i in range(0, len(l) - 1, 2):
#         l[i], l[i + 1] = l[i + 1], l[i]
#     return "".join(l)


def odd_even_swap(word):
    w, l = word, len(word) - 1
    return "".join(w[i + 1] + w[i] for i in range(0, l, 2)) + ((l + 1) % 2) * word[l]
