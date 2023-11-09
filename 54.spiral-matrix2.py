#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, columns = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows - 1, 0, columns - 1
        ans = []
        
        while len(ans) < rows * columns:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                for i in range(right,left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top -1, -1):
                    ans.append(matrix[i][left])
                left += 1
            
        return ans
# @lc code=end

