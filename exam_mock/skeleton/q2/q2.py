# from math import inf, sqrt


# def closest_pair(coord_list):
#     s = (inf,)
#     for a in coord_list:
#         for b in coord_list:
#             if a != b:
#                 d = 0
#                 for i, va in enumerate(a):
#                     d += (va - b[i]) ** 2
#                 s = min(s, (sqrt(d), a, b), key=lambda x: x[0])
#     return {s[1], s[2]}

from math import sqrt


def closest_pair(coord_list):
    s = set()
    for i, a in enumerate(coord_list):
        for b in map(lambda x: coord_list[x], range(i + 1, len(coord_list))):
            s.add((sqrt(sum(map(lambda x: (x[0] - x[1]) ** 2, zip(a, b)))), a, b))
    return list(map(lambda x: {x[1], x[2]}, [min(s, key=lambda x: x[0])]))[0]
