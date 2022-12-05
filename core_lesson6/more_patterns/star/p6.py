"""Pattern
      *   
     *  *   
    *  *  *   
   *  *  *  *   
  *  *  *  *  *   
 *  *  *  *  *  *   
*  *  *  *  *  *  *  
"""

r = 7
[print(" " * (r - i) + "*  " * (i + 1)) for i in range(r)]
