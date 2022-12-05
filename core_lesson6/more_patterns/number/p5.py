""" Pattern
1
3 3
5 5 5
7 7 7 7
9 9 9 9 9
"""

r = 5
[print((str(i * 2 - 1) + " ") * i) for i in range(1, r + 1)]
