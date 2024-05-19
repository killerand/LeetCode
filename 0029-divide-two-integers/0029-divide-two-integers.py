class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle the special case of overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the quotient
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        # Count how many times the divisor can be subtracted from the dividend
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple
        
        # Apply the sign to the quotient
        if negative:
            quotient = -quotient
        
        # Ensure the quotient is within the 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, quotient))
        