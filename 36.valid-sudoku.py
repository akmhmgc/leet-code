#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def ok(li):
            nums = [int(i) for i in li if i  != '.']
            return len(nums) == len(set(nums))
        flag = True

        # rows
        for row in board:
            flag &= ok(row)
        
        # columns
        for i in range(9):
            column = []
            for row in board:
                column.append(row[i])
            flag &= ok(column)

        # 3*3
        for i in range(0,9,3):
            for j in range(0,9,3):
                li = []
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        li.append(board[k][l])
                
                flag &= ok(li)
        return flag        
# @lc code=end

