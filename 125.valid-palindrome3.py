#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l + 1, r - 1
        return True
            
    def alphaNum(self, s):
        return (ord('a') <= ord(s) <= ord('z') or
                ord('A') <= ord(s) <= ord('Z') or 
                ord('0') <= ord(s) <= ord('9'))
# @lc code=end

