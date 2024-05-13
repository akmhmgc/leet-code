#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
        # 計算量は　nlog(n)になりうる
        sortedCounter = sorted(list(counter.items()), key=lambda x: x[1] * (-1))
        return [i[0] for i in sortedCounter][:k]
# @lc code=end

