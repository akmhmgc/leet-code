#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_index = 0
        for i in range(n):
            if i > max_index: break
            max_index = max(i + nums[i], max_index)
            if max_index >= n - 1: return True
        
        return False
            
# @lc code=end

