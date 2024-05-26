class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with -1 to handle edge cases
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        
        return max_length