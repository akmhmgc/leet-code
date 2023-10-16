#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        list = [''] * numRows
        n = len(s)
        print(n)
        i = 0
        while True:
            if i > n - 1: break
            for j in range(0, numRows):
                print(f'{i}: {list}')
                list[j] += s[i]
                i += 1
                if i > n - 1: break

            for j in range(numRows - 2, 0, -1):
                print(f'{i}: {list}')
                list[j] += s[i]
                i += 1
                if i > n - 1: break
        return ''.join(list)
            

# @lc code=end

