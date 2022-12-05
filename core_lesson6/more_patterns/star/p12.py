"""pattern
     * 
    * *
   *   *
  *     *
 *       *
*         *
 *       *
  *     *
   *   *
    * *
     * 
"""

r = 6
[print(" " * (s := abs(r - i)) + "* " + "  " * (r - s - 2) + "*" * (r - s > 1))
 for i in range(1, r * 2)]
