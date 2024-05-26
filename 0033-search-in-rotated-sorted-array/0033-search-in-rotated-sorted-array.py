class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # Use len(nums) instead of nums.length
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if the mid element is the target
            if nums[mid] == target:
                return mid
            
            # Determine which side is properly sorted
            if nums[left] <= nums[mid]:  # Left side is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Right side is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1