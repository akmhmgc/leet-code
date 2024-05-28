#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        l = 0
        maxF = 0
        charCount = defaultdict(int)
        for r in range(len(s)):
            charCount[s[r]] += 1
            maxF = max(maxF, charCount[s[r]])
            while r - l + 1 - maxF > k:
                charCount[s[l]]-= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
# @lc code=end

