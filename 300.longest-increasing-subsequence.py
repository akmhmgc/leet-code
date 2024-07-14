#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i]: i番目を必ず先頭として含むnums[i:n]のlongest strictly increasing subarray
        dp = [1] * n 

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
            
# @lc code=end

