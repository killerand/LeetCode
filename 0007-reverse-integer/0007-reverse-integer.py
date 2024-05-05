class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        reversed_num = 0
        
        # Reverse the integer
        reversed_num = int(str(abs(x))[::-1])
        
        # Check if reversed integer falls within 32-bit range
        if reversed_num > INT_MAX or reversed_num < INT_MIN:
            return 0
        
        # Restore the sign
        if x < 0:
            reversed_num *= -1
            
        return reversed_num
