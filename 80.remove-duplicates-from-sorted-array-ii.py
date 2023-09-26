#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 2: return length
        k = 2
        i = 2
        v1 = nums[0]
        v2 = nums[1]
        while i < length:
            if v1 == v2 and v1 == nums[i]:
                nums[i] = 10**5
            else:
                v1 = v2
                v2 = nums[i]
                k += 1
            i += 1
        nums.sort()
        return k
        
# @lc code=end

