#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1] * length
        for i in range(length - 1):
            ans[i + 1] = ans[i] * nums[i]
        right = nums[-1]
        for i in range(length - 2 , -1 ,-1):
            ans[i] = ans[i] * right
            right = right* nums[i]
        return ans

# @lc code=end

