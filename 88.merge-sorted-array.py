#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m + n):
            if len(nums2) == 0: continue
            if nums1[i] < nums2[0]: continue
            nums1.insert(i, nums2[0])
            nums2.pop(0)
        for i in range(n):
            nums1.pop(-1)
        for i in nums2:
            nums1.append(i)
# @lc code=end

