class Solution(object):
    def intToRoman(self, num):
        # Define symbols and their corresponding values
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        # Initialize an empty string to store the Roman numeral
        roman_numeral = ''
        
        # Iterate through symbols and values
        i = 0
        while num > 0:
            # Subtract the largest possible value and append the corresponding symbol
            while num >= values[i]:
                num -= values[i]
                roman_numeral += symbols[i]
            i += 1
        
        return roman_numeral

# Test the function
solution = Solution()
print(solution.intToRoman(3549))  # Output: MMMDXLIX
