def odd_even_swap(word):
    l = list(word)
    for i in range(0, len(l) - 1, 2):
        l[i], l[i + 1] = l[i + 1], l[i]
    return "".join(l)
