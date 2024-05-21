class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j] will be True if the first i characters in s
        # match the first j characters in p
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns with '*' that can match zero elements
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' can match zero of the preceding element
                    dp[i][j] = dp[i][j - 2] or \
                               (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    # Exact match or match with '.'
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        
        return dp[m][n]
        