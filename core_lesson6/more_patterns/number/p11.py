from math import factorial as f

r = 9
[print(" ".join(str(f(i) // (f(j) * f(i - j)))
       for j in range(i + 1))) for i in range(r)]
