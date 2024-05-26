#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        res = 0
        l,r = 0, len(height) - 1
        while l < r:
            heightL, heightR = height[l], height[r]
            res = max(res, min(heightL, heightR) * (r - l))
            if heightL < heightR:
                l += 1
            else:
                r -= 1
        return res
    
# @lc code=end

