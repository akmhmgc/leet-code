#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        first = gas[0] - cost[0]
        diffs = [first]
        cumsum = [first]
        for i in range(1,n):
            diff = gas[i] - cost[i]
            diffs.append(diff)
            cumsum.append(cumsum[i-1] + diff)
        if sum(diffs) < 0: return -1

        ans = 0
        max = -1
        for i in range(n):
            d = diffs[i] - cumsum[i]
            if max < d:
                max = d
                ans = i
        return ans
# @lc code=end

