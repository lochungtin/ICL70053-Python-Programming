""" Pattern
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
"""

r = 5
[print((str(i + 1) + " ") * (r - i)) for i in range(r)]
