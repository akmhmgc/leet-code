#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]: iを構成するための最少のコインの枚数
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
        print(dp)
        return dp[-1] if not dp[-1] == float("inf") else -1
# @lc code=end

