#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        end = 0
        farthest = 0
        n = len(nums)
        for i in range(n - 1):
            farthest = max(farthest, nums[i] + i)
            if farthest >= n - 1:
                ans += 1
                break
            
            if i == end:
                ans += 1
                end = farthest
        return ans
            
# @lc code=end

