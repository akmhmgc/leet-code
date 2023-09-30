#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 最大で到達できる場所を更新していく
        reachable = 0
        for i in range(len(nums)):
            if reachable < i: return False
            reachable = max(reachable, i + nums[i])
        return True
# @lc code=end

