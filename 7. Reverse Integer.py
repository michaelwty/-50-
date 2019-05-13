# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        strX = ''
        if x < 0:
            strX = str(x)[1:]
        else:
            strX = str(x)
            
        strX = strX[::-1]
        
        if int(strX) > 2**31-1:
            return 0
        elif x < 0:
            return -int(strX)        
        else:
            return int(strX)
        
        