class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize result array to store intermediate results
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Reverse the strings to make it easier to multiply from right to left
        num1, num2 = num1[::-1], num2[::-1]
        
        # Multiply each digit and add the results to the result array
        for i in range(m):
            for j in range(n):
                result[i + j] += int(num1[i]) * int(num2[j])
                result[i + j + 1] += result[i + j] // 10  # Handle carry
                result[i + j] %= 10  # Keep only the last digit
        
        # Remove leading zeros and convert to string
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        # Convert the result array back to string
        return ''.join(map(str, result[::-1]))

