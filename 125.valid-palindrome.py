#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted_s = ''
        for l in s:
            if l.isalnum(): converted_s+= l.lower()

        length = len(converted_s)
        for i in range(length // 2):
            if converted_s[i] != converted_s[length - 1 - i]:
                return False
        return True
# @lc code=end

