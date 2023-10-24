#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        sum = 0
        left = 0
        for i, vi in enumerate(nums):
            sum += vi
            while sum >= target:
                ans = min(ans, i - left + 1)
                sum -= nums[left]
                left += 1
        return ans % (len(nums) + 1)
# @lc code=end

