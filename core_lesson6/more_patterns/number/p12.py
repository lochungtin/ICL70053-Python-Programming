""" Pattern
1 2 3 4 5
2 2 3 4 5
3 3 3 4 5
4 4 4 4 5
5 5 5 5 5
"""

r = 5
[print(" ".join(str((i > j) * i + (i <= j) * j)for j in range(1, r + 1)))
 for i in range(1, r + 1)]
