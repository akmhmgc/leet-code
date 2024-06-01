#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        for c in s:
            if stack and closeToOpen.get(c, "") == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
# @lc code=end

