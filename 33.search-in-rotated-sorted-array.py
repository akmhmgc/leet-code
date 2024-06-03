#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        index = -1
        while l <= r:
            m = (l + r) // 2
            print(l,m,r)
            if nums[l] <= nums[m]:
               if nums[l] <= target and target <= nums[m]:
                   return self.binarySearch(l,r, nums, target)
               else:
                   l = m + 1
            else:
               if nums[m] <= target and target <= nums[r]:
                return self.binarySearch(l,r, nums, target)
               else:
                   r = m - 1
        return index
    def binarySearch(self, l:int, r:int, nums: List[int], target: int) -> int:
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] >  target:
                r = m - 1
            else:
                l = m + 1
        return -1
# @lc code=end

