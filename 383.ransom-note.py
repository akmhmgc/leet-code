#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter, magazine_counter = Counter(ransomNote), Counter(magazine)
        return ransom_counter & magazine_counter == ransom_counter
# @lc code=end

