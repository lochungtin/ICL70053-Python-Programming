""" Pattern
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
"""

r = 5
[print(" ".join(str(j) for j in range(r + 1 - i))) for i in range(r)]
