#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of anagrams
        for s in strs:
            charCount = [0] * 26
            for c in s:
                charCount[ord(c) - ord('a')] += 1
            res[tuple(charCount)].append(s)
        return res.values()

# @lc code=end

