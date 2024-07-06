#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1: return 1
        dp = [[False] * n] * n
        for i in range(n):
            dp[i][i] = True

        # チェックするウィンドウの幅
        for length in range(2, n + 1):
            # ウィンドウ開始する場所
            for i in range(n - length):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or dp[i+1][j-1]):
                    dp[i][j] = True
        count = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j] == True: count += 1
        return count
# @lc code=end

