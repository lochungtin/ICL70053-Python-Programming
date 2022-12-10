def count_repeats(word):
    freq = {}
    for char in word:
        freq[char] = freq.get(char, 0) + 1

    counts = freq.values()
    if len(counts) > 0:
        n = list(counts)[0]
        for count in counts:
            if count != n:
                return 0
        return n
    else:
        return 0
