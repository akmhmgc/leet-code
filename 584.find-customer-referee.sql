--
-- @lc app=leetcode id=584 lang=mysql
--
-- [584] Find Customer Referee
--

-- @lc code=start
# Write your MySQL query statement below
select name
  from Customer
  where referee_id is null 
  or referee_id != 2


-- @lc code=end

