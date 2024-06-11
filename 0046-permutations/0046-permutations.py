class Solution:
    def permute(self, nums):
        def backtrack(start, end):
            # If we've reached the end of the list, add the permutation to the results
            if start == end:
                result.append(nums[:])
            for i in range(start, end):
                # Swap the current element with the start
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse on the remaining elements
                backtrack(start + 1, end)
                # Backtrack: undo the swap
                nums[start], nums[i] = nums[i], nums[start]
        
        result = []
        backtrack(0, len(nums))
        return result
        