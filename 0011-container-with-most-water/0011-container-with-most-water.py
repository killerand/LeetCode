class Solution:
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculate the area between the two lines
            area = min(height[left], height[right]) * (right - left)
            # Update max_area if the current area is greater
            max_area = max(max_area, area)

            # Move the pointer with the shorter line towards the other pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


        