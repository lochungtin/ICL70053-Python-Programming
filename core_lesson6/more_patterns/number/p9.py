""" Pattern
1 
3 2 
6 5 4 
10 9 8 7 
15 14 13 12 11
"""

r = 5
[print(" ".join(str(sum(range(i)) + i - j) for j in range(i)))
 for i in range(1, r + 1)]
