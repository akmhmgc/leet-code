#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = prices[0]
        i = 0
        while i < len(prices):
            current_value = prices[i]
            min_value = min(min_value, current_value)
            max_profit = max(max_profit, current_value - min_value)
            i += 1
        return max_profit

# @lc code=end

