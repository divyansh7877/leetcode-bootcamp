class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #Create a list of false for DP
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1): # Move from end to start
            for w in wordDict:
                lw = len(w)
                if (i+lw) <= len(s) and s[i:i+lw] == w:
                    dp[i] = dp[i+ lw ]
                if dp[i]:
                    break
        return dp[0]