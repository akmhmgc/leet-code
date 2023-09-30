#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        max_profit = 0
        while i < len(prices):
            profit = prices[i] - prices[i - 1]
            if profit > 0: max_profit += profit
            i += 1
        return max_profit
        
# @lc code=end

