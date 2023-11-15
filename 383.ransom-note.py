#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        flag = True
        for k in ransom_counter:
            if ransom_counter[k] > magazine_counter[k]: flag = False
        return flag
# @lc code=end

