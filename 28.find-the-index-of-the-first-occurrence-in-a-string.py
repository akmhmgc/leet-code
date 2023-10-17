#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = -1
        for i in range(len(haystack)):
            if haystack[i] != needle[0]: continue
            if i + len(needle) > len(haystack): break

            flag = True
            for j in range(i, i + len(needle)):
                if haystack[j] != needle[j - i]: flag = False
            
            if flag:
                ans = i
                break
        return ans
# @lc code=end

