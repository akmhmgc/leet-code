#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int])ww -> int:
        sorted_citatios = sorted(citations)
        n = len(citations)
        for i in range(n):
            index = len(sorted_citatios) - i
            if sorted_citatios[i] >= index:
                return index
        return 0
        
# @lc code=end

