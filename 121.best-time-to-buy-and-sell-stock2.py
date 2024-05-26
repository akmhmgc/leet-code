#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minValue = prices[0]
        for p in prices:
            minValue = min(minValue, p)
            res = max(res, p - minValue)
        return res
# @lc code=end

