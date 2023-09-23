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
  len = nums.length
  i = 0
  while i < len
    j = i + 1
    while j < len
      if nums[i] + nums[j] == target
        return [i, j]
      end
      j += 1
    end
    i += 1
  end
end
# @lc code=end

