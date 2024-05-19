class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Lengths of haystack and needle
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        # Edge case: if needle is an empty string, return 0
        if needle_len == 0:
            return 0
        
        # Iterate through the haystack
        for i in range(haystack_len - needle_len + 1):
            # Check if the substring of haystack starting at index i matches needle
            if haystack[i:i + needle_len] == needle:
                return i
        
        # If needle is not found in haystack, return -1
        return -1

        