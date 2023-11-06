--
-- @lc app=leetcode id=180 lang=mysql
--
-- [180] Consecutive Numbers
--

-- @lc code=start
# Write your MySQL query statement below
select
  id,
  num
  rank() over (ORDER BY id) as ranking
  from ConsecutiveNums
-- @lc code=end

