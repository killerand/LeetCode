class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub = {}
        cur_sub_start = 0
        cur_len = 0
        longest = 0

        for i, letter in enumerate(s):
            if letter in sub and sub[letter] >= cur_sub_start:
                cur_sub_start = sub[letter] + 1
                cur_len = i - sub[letter]
                sub[letter] = i
            else:
                sub[letter] = i
                cur_len += 1
                if cur_len > longest:
                    longest = cur_len

        return longest