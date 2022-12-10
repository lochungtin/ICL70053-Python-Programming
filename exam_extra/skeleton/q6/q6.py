# def freq(filename):
#     count = {}
#     with open("q6/" + filename, "r") as f:
#         for line in f.readlines():
#             for word in line.strip().split(" "):
#                 if word not in count:
#                     count[word] = 1
#                 else:
#                     count[word] += 1
#     return count
# def most_frequent_common_word(filename1, filename2):
#     f1 = freq(filename1)
#     f2 = freq(filename2)
#     avg = []
#     for word, f1freq in f1.items():
#         if word in f2:
#             avg.append((word, (f1freq + f2[word]) / 2))
#     return sorted(avg, key=lambda x: x[1], reverse=True)[0]


def most_frequent_common_word(filename1, filename2):
    c = {}
    for f in (filename1, filename2):
        for l in open("q6/" + f, "r"):
            [c.update({w: c.get(w, 0) + 0.5}) for w in l.strip().split(" ")]
    return sorted(c.items(), key=lambda x: x[1], reverse=True)[0]
