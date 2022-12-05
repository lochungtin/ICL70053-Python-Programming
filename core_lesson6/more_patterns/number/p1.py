""" Pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

r = 5
[print(" ".join(str(j + 1) for j in range(i + 1))) for i in range(r)]
