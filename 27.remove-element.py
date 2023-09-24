#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        for i in range(len(nums)):
            num = nums[i]
            if num != val:
                ans += 1
                continue
            nums[i] = 200
        nums.sort()
        return ans
        
# @lc code=end

