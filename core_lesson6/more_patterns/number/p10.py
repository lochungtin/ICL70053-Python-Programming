""" Pattern
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 
"""

r = 5
[print("  " * (r - i) + " ".join(str(j + 1) for j in range(i)))
 for i in range(1, r + 1)]
