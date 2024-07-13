#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dpMax = [1] * (n + 1)
        dpMin = [1] * (n + 1)
        for i in range(n):
            num = nums[i]
            if num >=0:
                dpMax[i + 1] = max(dpMax[i] * num, num)
                dpMin[i + 1] = min(dpMin[i] * num, num)
            else:
                dpMax[i + 1] = max(dpMin[i] * num, num)
                dpMin[i + 1] = min(dpMax[i] * num, num)

        return max(dpMax[1:])
# @lc code=end

