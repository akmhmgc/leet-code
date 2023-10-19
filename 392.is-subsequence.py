#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 : return True
        if len(t) == 0 : return False
        i = 0
        j = 0
        while True:
            if s[i] == t[j]:
                i,j = i + 1 , j + 1
            else:
                j += 1

            if i == len(s):
                return True
            elif j == len(t):
                return False
        
# @lc code=end

