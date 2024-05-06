class Solution(object):
    def myAtoi(self, s):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Remove leading whitespace
        s = s.strip()
        
        # Check for empty string
        if not s:
            return 0
        
        # Check for sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        # Skip leading non-digit characters
        for char in s:
            if not char.isdigit():
                break
        
        # Convert numerical digits
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
        
        # Apply sign and check for overflow/underflow
        result *= sign
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result
