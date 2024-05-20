#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerS = ""
        for l in s:
            if l.isalnum(): lowerS+= l.lower()
        for i in range(len(lowerS) // 2):
            if lowerS[i] != lowerS[len(lowerS) - 1 - i]: return False
        return True
# @lc code=end

