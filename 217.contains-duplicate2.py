#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for i,j in zip(sorted_nums, sorted_nums[1:]):
            if i == j:
                return True
        return False
# @lc code=end

