class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the array to use two-pointer technique
        nums.sort()
        n = len(nums)
        result = []
        
        # Iterate over the first element
        for i in range(n - 3):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Iterate over the second element
            for j in range(i + 1, n - 2):
                # Skip duplicate values for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Use two-pointer technique for the remaining part of the array
                left = j + 1
                right = n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        # Add the quadruplet to the result
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip duplicate values for the third element
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicate values for the fourth element
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return result
        