class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, used):
            # If the current path is of the same length as nums, we have a complete permutation
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                # Skip used elements
                if used[i]:
                    continue
                
                # Skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                # Mark the number as used
                used[i] = True
                path.append(nums[i])
                
                # Recurse
                backtrack(path, used)
                
                # Unmark the number (backtrack)
                used[i] = False
                path.pop()
        
        # Sort nums to handle duplicates
        nums.sort()
        result = []
        used = [False] * len(nums)
        backtrack([], used)
        return result
        