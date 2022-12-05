"""Pattern
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * *
"""

r = 5
[print(" " * (s := r - abs(i - r) - (i >= r)) + "* " * (r - s))
 for i in range(r * 2)]
