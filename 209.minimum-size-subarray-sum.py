#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        left = 0
        right = 0
        sum = nums[0]
        while left <= right and left < len(nums) and right < len(nums):
            if sum < target and right == len(nums) - 1: break

            if sum < target:
                right +=1
                sum += nums[right]
            else:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1
        return 0 if ans == len(nums) + 1 else ans
# @lc code=end

