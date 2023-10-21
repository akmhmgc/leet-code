#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        remains = {}
        for i, num in enumerate(numbers, 1):
            remain = target - num
            if num in remains:
                return [remains[num], i]
            else:
                remains[remain] = i
# @lc code=end

