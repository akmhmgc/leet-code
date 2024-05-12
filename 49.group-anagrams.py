#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in sortedStrs:
                sortedStrs[sorted_str].append(str)
            else:
                sortedStrs[sorted_str] = [str]
        return list(sortedStrs.values())

# @lc code=end

