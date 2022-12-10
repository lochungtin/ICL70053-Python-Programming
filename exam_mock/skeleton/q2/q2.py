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


def closest_pair(coord_list):
    d = [((a, b), zip(a, b)) for a in coord_list for b in coord_list if a != b]
    return set(min(((sum(map(lambda x: (x[0] - x[1]) ** 2, q)), p)) for p, q in d)[1])
