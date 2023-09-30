#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True

        i = len(nums) - 2
        min_step = 1
        flag = True
        while i >= 0:
            if nums[i] < min_step:
                min_step += 1
                flag = False
            else:
                min_step = 1
                flag = True
            i -= 1
        return flag
# @lc code=end

