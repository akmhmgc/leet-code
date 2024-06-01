#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        rest = []
        for c in s:
            if c == ")" and len(rest) > 0 and rest[-1] == "(":
                rest.pop()
            elif c == "]" and len(rest) > 0 and rest[-1] == "[":
                rest.pop()
            elif c == "}" and len(rest) > 0 and rest[-1] == "{":
                rest.pop()
            else:
                rest.append(c)
        return len(rest) == 0
# @lc code=end

