#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_s = Counter(s)
        for k in count_t:
            if count_s[k] < count_t[k]: return ""
        if len(t) == 1: return t
        remain = len(t)
        ans = [0,len(s) - 1]
        left = 0
        
        for i,vi in enumerate(s):
            if not vi in count_t: continue
            
            count_t[vi] -= 1
            if count_t[vi] >= 0: remain-= 1
            
            if remain == 0:
                for j in range(left, i + 1):
                    vj = s[j]
                    if not vj in count_t: continue

                    if count_t[vj] >= 0:
                        if remain == 0:
                            if ans[1] - ans[0] >= i - j:
                                ans = [j, i]
                        if remain == 1:
                            left = j
                            break
                        remain += 1


                    count_t[vj] += 1
        return s[ans[0]:ans[1] + 1]

# @lc code=end

