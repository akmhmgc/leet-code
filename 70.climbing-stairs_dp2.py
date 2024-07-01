#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
# 配るdpで解いたパターン
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(0, n - 1):
            dp[i + 1] += dp[i]
            dp[i + 2] += dp[i]
        return dp[-1]
# @lc code=end

