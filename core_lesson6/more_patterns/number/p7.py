""" Pattern
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""

r = 5
[print(" ".join(str(i - j) for j in range(i))) for i in range(1, r + 1)]
