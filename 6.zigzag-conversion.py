#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s

        list = [''] * numRows
        index = 0
        for st in s:
            if index == 0: step = 1
            if index == numRows - 1: step = -1
            list[index] += st
            index += step
        return ''.join(list)

# @lc code=end

