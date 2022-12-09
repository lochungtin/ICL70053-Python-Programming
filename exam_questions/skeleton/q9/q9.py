# def factors(num):
#     rt = []
#     for n in range(1, num // 2 + 1):
#         if num % n == 0:
#             rt.append(n)
#             rt.append(num // n)

#     return sorted(list(set(rt)), reverse=True)


# def simplify_fraction(numerator, denominator):
#     nFact = factors(numerator)
#     dFact = factors(denominator)

#     for n in nFact:
#         if n in dFact:
#             return (numerator // n, denominator // n)

#     return (numerator, denominator)


def simplify_fraction(numerator, denominator):
    n = set([n for n in range(1, numerator + 1) if numerator % n == 0])
    d = set([n for n in range(1, denominator + 1) if denominator % n == 0])
    c = sorted(n & d, reverse=True)[0]
    return numerator // c, denominator // c
