""" Pattern
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""

r = 5
[print(" ".join(str(i - j) for j in range(i))) for i in range(r, 0, -1)]
