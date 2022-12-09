# def minmax_swap(number):
#     numList = list(map(lambda x: int(x), str(number)))

#     minNum = number
#     maxNum = number

#     size = len(numList)
#     for i in range(size):
#         for j in range(i + 1, size):
#             mutable = list(numList)
#             mutable[i], mutable[j] = numList[j], numList[i]

#             if mutable[0] == 0:
#                 continue

#             newNum = int("".join(map(lambda x: str(x), mutable)))

#             minNum = min(minNum, newNum)
#             maxNum = max(maxNum, newNum)

#     return (minNum, maxNum)


def minmax_swap(number):
    c = set()
    for i, h in enumerate(str(number)):
        for j, k in enumerate(str(number)):
            m, m[i], m[j] = list(str(number)), k, h
            if m[0] != "0":
                c.add(int("".join(m)))
    return min(c), max(c)
