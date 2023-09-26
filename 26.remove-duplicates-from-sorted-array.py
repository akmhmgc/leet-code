#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        val = nums[0]
        i = 1
        k = 1
        while i < len(nums):
            if nums[i] == val:
                nums[i] = 200
            else:
                val = nums[i]
                k += 1
            i += 1
        nums.sort()
        return k
        
# @lc code=end

