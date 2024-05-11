#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexOfNums = {}
        for i in range(len(nums)):
            if target - nums[i] in indexOfNums:
                return [indexOfNums[target - nums[i]], i]
            else:
                indexOfNums[nums[i]] = i
# @lc code=end
