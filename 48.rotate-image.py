#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 1: return matrix

        n = len(matrix)
        left,right = 0, n - 1
        for i in range(math.floor(n / 2)):
            for j in range(left, right):
                points = [
                    [i,j],
                    [j, n - 1 - i],
                    [n - 1 - i, n - j - 1],
                    [n - j - 1, i]   
                ]
                val = []
                for k in range(-1,3):
                    x, y = points[k]
                    val.append(matrix[x][y])
                print(val)
                for k in range(4):
                    x, y = points[k]
                    matrix[x][y] = val[k]
            left += 1
            right -= 1
        return matrix
# @lc code=end

