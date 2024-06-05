class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Place each number in its right place if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the number at its target position
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # Find the first position where the number is not correct
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all positions are correct, the missing number is n + 1
        return n + 1