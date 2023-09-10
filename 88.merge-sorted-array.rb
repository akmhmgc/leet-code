#
# @lc app=leetcode id=88 lang=ruby
#
# [88] Merge Sorted Array
#

# @lc code=start
# @param {Integer[]} nums1
# @param {Integer} m
# @param {Integer[]} nums2
# @param {Integer} n
# @return {Void} Do not return anything, modify nums1 in-place instead.
def merge(nums1, m, nums2, n)
  n.times do |i|
    nums1[-1 + (-1) * i] = nums2[i]
  end
  nums1.sort!
end
# @lc code=end

