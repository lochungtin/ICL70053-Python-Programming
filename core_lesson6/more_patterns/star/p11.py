"""pattern
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
"""

r = 6
[print(" " * (s := abs(r - i)) + "* " * (r - s)) for i in range(1, r * 2)]
