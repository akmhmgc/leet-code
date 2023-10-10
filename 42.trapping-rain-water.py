#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        water = [0] * n
        for i in range(n):
            if height[left] <= height[i]:
                for j in range(left + 1, i):
                    water[j] = height[left]
                left = i

        right = -1
        for i in range(n - 1, -1, -1):
            if height[right] <= height[i]:
                for j in range(right - 1, i, -1):
                    water[j] = height[right]
                right = i
        
        ans = 0
        for i in range(n):
            if water[i] > height[i]: ans += water[i] - height[i]
        return ans
        
            
# @lc code=end

