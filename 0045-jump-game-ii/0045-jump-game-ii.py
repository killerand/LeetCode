class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            # When we reach the end of the current range
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # If the farthest point we can reach is already the last index, we can stop
                if current_end >= len(nums) - 1:
                    break

        return jumps
    
        