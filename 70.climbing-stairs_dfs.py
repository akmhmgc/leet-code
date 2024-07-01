#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    steps = {}
    def climbStairs(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 1

        if not n - 1 in self.steps:
            self.steps[n - 1] = self.climbStairs(n - 1)
        if not n - 2 in self.steps:
            self.steps[n - 2] = self.climbStairs(n - 2)

        return self.steps[n - 1] + self.steps[n - 2] 
# @lc code=end

