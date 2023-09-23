#
# @lc app=leetcode id=1 lang=ruby
#
# [1] Two Sum
#

# @lc code=start
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  sorted = nums.sort
  len = sorted.length
  i = 0
  while i < len
    val1 = sorted[i]
    val2 = sorted[(i+1)..-1].bsearch { |x| x >= target - sorted[i] }
    if val2 && val1 + val2 == target
      vals = [val1, val2]
      break
    end
    i += 1
  end
  [nums.index(vals[0]), nums.rindex(vals[1])]
end
# @lc code=end
