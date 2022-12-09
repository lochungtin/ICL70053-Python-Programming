"""Pattern
. . . . *
. . . *
. . *
. *
*
. *
. . *
. . . *
. . . . *
"""

r = 9
[print(". " * abs(r // 2 - i) + "*") for i in range(r)]
