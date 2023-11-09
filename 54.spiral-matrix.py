#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        gone = [[False] * n for i in range(m)]
        gone[0][0] = True

        def turn(x,y):
            if (x, y) == (0, 1): return (1, 0)
            if (x, y) == (1, 0): return (0, -1)
            if (x, y) == (0, -1): return (-1, 0)
            if (x, y) == (-1, 0): return (0, 1)

        x,y = 0,0
        dx, dy = 0,1
        ans = [matrix[x][y]]

        while True:
            if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n and gone[x + dx][y + dy] == False:
                x+= dx
                y+= dy
                matrix[x][y]
                gone[x][y] = True
                ans.append(matrix[x][y])
                continue
            dx, dy = turn(dx,dy)
            if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n and gone[x + dx][y + dy] == False:
                x+= dx
                y+= dy
                matrix[x][y]
                gone[x][y] = True
                ans.append(matrix[x][y])
                continue
            break
        return ans
# @lc code=end

