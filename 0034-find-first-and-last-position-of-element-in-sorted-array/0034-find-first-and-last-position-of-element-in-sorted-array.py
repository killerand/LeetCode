class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirstPosition(nums, target):
            left, right = 0, len(nums) - 1
            first_pos = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    first_pos = mid
                    right = mid - 1  # Keep searching to the left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first_pos
        
        def findLastPosition(nums, target):
            left, right = 0, len(nums) - 1
            last_pos = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    last_pos = mid
                    left = mid + 1  # Keep searching to the right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last_pos
        
        first_pos = findFirstPosition(nums, target)
        if first_pos == -1:
            return [-1, -1]  # Target not found
        last_pos = findLastPosition(nums, target)
        return [first_pos, last_pos]