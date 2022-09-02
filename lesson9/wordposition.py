def get_word_positions(words):
    rt = {}

    for index, word in enumerate(words):
        if word not in rt:
            rt[word] = []

        rt[word].append(index)

    return rt


words = [
    "feelings",
    "feelings",
    "like",
    "i've",
    "never",
    "lost",
    "you",
    "and",
    "feelings",
    "like",
    "i've",
    "never",
    "have",
    "you",
]
positions = get_word_positions(words)
print(positions)
