#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m for i in range(n)]
        dp[0][0] = 1

        for i in range(n):
            for j in range(m):
                if i - 1 >=  0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 >=  0:
                    dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]
# @lc code=end

