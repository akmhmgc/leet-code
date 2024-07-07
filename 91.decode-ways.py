#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0

        one,two = 1,1

        def valid(str):
            if str[0] == "0":
                return False
            else:
                return 1 <= int(str) and int(str) <= 26

        n = len(s)
        for i in range(1, n):
            tmp = two
            two = 0
            if valid(s[i]):
                two += tmp
            if valid(s[i-1:i+1]):
                two += one
            one = tmp
        return two
    
# @lc code=end

