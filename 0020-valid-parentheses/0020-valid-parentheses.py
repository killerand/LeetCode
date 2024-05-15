class Solution:
    def isValid(self, s: str) -> bool:
        # A stack to keep track of opening brackets
        stack = []
        # A mapping of closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the string
        for char in s:
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the top element doesn't match the corresponding opening bracket, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)
        
        # If the stack is empty, all the opening brackets have been matched
        return not stack
