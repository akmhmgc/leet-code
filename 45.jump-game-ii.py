#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        min_steps = [10**10] * n
        min_steps[0] = 0
        for i in range(n):
            current_step = min_steps[i]
            if current_step == 10 ** 10 : continue

            for j in range(i, min(nums[i] + i + 1, n)):
                min_steps[j] = min(min_steps[j], current_step + 1)
        return min_steps[-1]
            
        
# @lc code=end

