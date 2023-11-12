#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, columns = len(board), len(board[0])
        def alive_cells_count(x,y):
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == j == 0: continue

                    nx, ny = x + i, y + j
                    if nx < 0 or nx >= rows or ny < 0 or ny >= columns: continue
                    
                    count += board[nx][ny]
            return count
        
        def current_state(cell, live_cells_count):
            if cell == 0:
                if live_cells_count == 3: return 1
                else:
                    return 0
            else:
                if live_cells_count < 2: return 0
                if live_cells_count >= 2 and live_cells_count <= 3 : return 1
                if live_cells_count > 3 : return 0
        states = [[0] * columns for i in range(rows)]
        for i in range(rows):
            for j in range(columns):
                cell = board[i][j]
                count = alive_cells_count(i,j)
                state = current_state(cell, count)
                states[i][j] = state
        for i in range(rows):
            for j in range(columns):
                board[i][j] = states[i][j]

# @lc code=end

