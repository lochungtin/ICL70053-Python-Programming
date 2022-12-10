def odd_even_swap(word):
    new_word = ""
    for i in range(0, len(word)-1, 2):
        new_word += word[i+1] + word[i]

    if len(word) % 2 == 1:
        new_word += word[-1]

    return new_word


def odd_even_swap_v2(word):
    new_word = list(word)
    for i in range(0, len(word)-1, 2):
        new_word[i], new_word[i+1] = new_word[i+1], new_word[i]
    return "".join(new_word)


