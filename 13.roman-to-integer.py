#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        values1 = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,'M': 1000 }
        values2 = { 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900 }
        ans = 0
        for pre, cur in zip(s[:-1], s[1:]):
            if f"{pre}{cur}" in values2:
                ans -= values1[pre]
            else:
                ans += values1[pre]
        return ans + values1[s[-1]]
# @lc code=end

