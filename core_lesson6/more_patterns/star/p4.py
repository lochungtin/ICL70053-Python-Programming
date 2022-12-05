"""Pattern
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     *
"""

r = 6
[print(" " * (i) + "* " * (r - i)) for i in range(r)]
