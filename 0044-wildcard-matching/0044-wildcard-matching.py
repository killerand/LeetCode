class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Lengths of the input string and the pattern
        s_len = len(s)
        p_len = len(p)
        
        # Initialize the DP table with False
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Handle patterns with '*' at the beginning
        for j in range(1, p_len + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
        
        # Fill the DP table
        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                if p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
        
        return dp[s_len][p_len]