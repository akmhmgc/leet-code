#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        min_word_length = 1000
        for word in strs:
            min_word_length = min(min_word_length, len(word))
        
        for i in range(min_word_length):
            s = set()
            for str in strs:
                s.add(str[i])
            if len(s) == 1:
                ans+= str[i]
            else:
                break
        return ans
                

