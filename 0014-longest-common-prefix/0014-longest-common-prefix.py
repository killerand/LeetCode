class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Sort the array of strings
        strs.sort()

        # Take the first and last strings (after sorting) to compare
        first = strs[0]
        last = strs[-1]

        # Find the common prefix between the first and last strings
        prefix = ""
        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                prefix += first[i]
            else:
                break

        return prefix

