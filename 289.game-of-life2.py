#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
  def gameOfLife(self, board: List[List[int]]) -> None:
    for i in range(len(board)):
      for j in range(len(board[0])):
        ones = 0
        # 自分自身も含めた周囲のセルを計算している
        for x in range(max(0, i - 1), min(len(board), i + 2)):
          for y in range(max(0, j - 1), min(len(board[0]), j + 2)):
            ones += board[x][y] & 1
        # Any live cell with 2 or 3 live neighbors
        # lives on to the next generation
        if board[i][j] == 1 and (ones == 3 or ones == 4):
          board[i][j] |= 2
        # Any dead cell with exactly 3 live neighbors
        # becomes a live cell, as if by reproduction
        if board[i][j] == 0 and ones == 3:
          board[i][j] |= 2

    for i in range(len(board)):
      for j in range(len(board[0])):
        # 右シフト
        board[i][j] >>= 1

# @lc code=end

