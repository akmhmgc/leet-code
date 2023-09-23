#
# @lc app=leetcode id=1 lang=ruby
#
# [1] Two Sum
#

# @lc code=start
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
# O(n log(n))
# sort the array (preserving original index), then two-pointer stategy
def two_sum(nums, target)
  map = {}
  i = 0
  while i < nums.length
    if map[target - nums[i]]
      return [map[target - nums[i]], i]
    else
      map[nums[i]] = i
    end
    i += 1
  end
end
# @lc code=end
