"""Pattern
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

r = 5
[print("* " * (r - abs(i - r))) for i in range(1, r * 2)]
