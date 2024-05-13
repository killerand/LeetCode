class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping from digits to letters
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # Helper function for backtracking
        def backtrack(combination, next_digits):
            # If there are no more digits to check
            if len(next_digits) == 0:
                # Add the combination to the result
                result.append(combination)
            else:
                # Iterate over all letters that the next digit maps to
                for letter in letters[next_digits[0]]:
                    # Call backtrack with the next digit removed and the current combination extended with the current letter
                    backtrack(combination + letter, next_digits[1:])

        # Initialize the result list
        result = []
        # Start the backtracking process with an empty combination and the input digits
        backtrack('', digits)
        return result

        