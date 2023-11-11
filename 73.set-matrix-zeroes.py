#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        empty_row_indexes, empty_column_indexes= set(), set()
        rows,columns = len(matrix), len(matrix[0])
        
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] != 0: continue
                
                empty_row_indexes.add(i)
                empty_column_indexes.add(j)
        
        for i in empty_row_indexes:
            for j in range(columns):
                matrix[i][j] = 0

        for i in range(rows):
            for j in empty_column_indexes:
                matrix[i][j] = 0
        return matrix
# @lc code=end

