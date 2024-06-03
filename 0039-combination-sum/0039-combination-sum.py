class Solution:
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()  # Optional: Helps in early stopping
        
        def backtrack(remaining, combo, start):
            if remaining == 0:
                result.append(list(combo))
                return
            elif remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # Include the candidate[i] in the combination
                combo.append(candidates[i])
                # Since the same number can be used multiple times, we pass `i` instead of `i + 1`
                backtrack(remaining - candidates[i], combo, i)
                # Backtrack, remove the number from the combination
                combo.pop()
        
        backtrack(target, [], 0)
        return result