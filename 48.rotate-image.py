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
        n = len(matrix)
        for i in range(math.ceil(n / 2)):
            for j in range(math.ceil(n / 2)):
                points = [
                    [i,j],
                    [j, n - 1 - i],
                    [n - 1 - i, n - j - 1],
                    [n - j - 1, i]   
                ]
                val = [matrix[x][y] for x,y in points]
                print(val)
                for k in range(4):
                    x, y = points[k]
                    matrix[x][y] = val[k - 1]
        return matrix
# @lc code=end

