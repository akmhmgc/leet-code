#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        distinct_words = set()
        for i in s:
            distinct_words.add(i)
            if i in hash_s:
                hash_s[i] += 1
            else:
                hash_s[i] = 1
        for i in t:
            distinct_words.add(i)
            if i in hash_t:
                hash_t[i] += 1
            else:
                hash_t[i] = 1
        for i in distinct_words:
            if i not in hash_s or i not in hash_t or hash_s[i] != hash_t[i]: return False
        return True
    
# @lc code=end

