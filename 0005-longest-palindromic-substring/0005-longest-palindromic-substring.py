class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        longest = ""
        for i in range(len(s)):
            # Check palindromes with center at index i
            palindrome_odd = self.expand_around_center(s, i, i)
            palindrome_even = self.expand_around_center(s, i, i + 1)
            longest = max(longest, palindrome_odd, palindrome_even, key=len)
        return longest

    def expand_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

