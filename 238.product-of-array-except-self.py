#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        suff = [1]
        n = len(nums)
        for i in range(n):
            pref.append(pref[i] * nums[i])
            suff.append(suff[i] * nums[n - i - 1])
        ans = []
        for i in range(n):
            ans.append(pref[i] * suff[n - i - 1])
        return ans

# @lc code=end

