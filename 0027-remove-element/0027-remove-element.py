class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer for the place to write the next element that is not val
        write_index = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_index] = nums[i]
                write_index += 1
        
        return write_index

        