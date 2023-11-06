--
-- @lc app=leetcode id=610 lang=mysql
--
-- [610] Triangle Judgement
--

-- @lc code=start
# Write your MySQL query statement below
# Write your MySQL query statement below

select
  x,y,z,
  case
  when x < y + z and y < x + z and z < x + y then 'Yes'
  else 'No'
  end triangle
  from Triangle
-- @lc code=end

