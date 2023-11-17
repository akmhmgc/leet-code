#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t, t_to_s = {}, {}
        for si,ti in zip(s,t):
            if si in s_to_t and s_to_t[si] != ti:
                return False
            elif ti in t_to_s and t_to_s[ti] != si:
                return False
            else:
                s_to_t[si] = ti
                t_to_s[ti] = si
        return True  
# @lc code=end

