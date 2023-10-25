#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        numbers = {}
        ans = 0
        left = 0
        for i, vi in enumerate(s):
            if vi in numbers and numbers[vi] >= left:
                left = numbers[vi] + 1
            numbers[vi] = i
            ans = max(ans, i - left + 1)
        return ans
        
# @lc code=end

