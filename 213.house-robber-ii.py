#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def robSub(nums):
            first,second = 0, 0
            for i in nums:
                tmp = second
                second = max(second, first + i)
                first = tmp
            return second
        
        if len(nums) == 1: return nums[0]

        return max(robSub(nums[1:]),robSub(nums[:-1]))
# @lc code=end

