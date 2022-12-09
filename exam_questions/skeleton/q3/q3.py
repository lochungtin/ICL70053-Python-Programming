# def count_repeats(word):
#     counts = {}

#     for letter in word:
#         if letter not in counts:
#             counts[letter] = 1
#         else:
#             counts[letter] += 1

#     val = list(counts.values())
#     num = val[0]

#     return val[0] * all(map(lambda x: x == num, val))


def count_repeats(word):
    c = {}
    [c.update({l: c.get(l, 0) + 1}) for l in word]
    return list(c.values())[0] * (len(set(c.values())) == 1)
