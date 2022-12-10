# def top5_bigram_frequency(filename):
#     with open("q3/" + filename) as f:
#         c = {}
#         for l in f.readlines():
#             splt = l.lower().strip().split(" ")
#             for i in range(len(splt) - 1):
#                 c[(splt[i], splt[i + 1])] = c.get((splt[i], splt[i + 1]), 0) + 1
#     return dict(
#         sorted(
#             [(" ".join(c), v) for c, v in c.items()], key=lambda x: x[1], reverse=True
#         )[0:5]
#     )


def top5_bigram_frequency(filename):
    c = {}
    for l in map(lambda x: x.strip().lower().split(" "), open("q3/" + filename)):
        for i in range(len(l) - 1):
            c[" ".join(l[i : i + 2])] = c.get(" ".join(l[i : i + 2]), 0) + 1
    return dict(sorted(c.items(), key=lambda x: x[1], reverse=True)[0:5])
