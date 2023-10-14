--
-- @lc app=leetcode id=577 lang=mysql
--
-- [577] Employee Bonus
--

-- @lc code=start
# Write your MySQL query statement below
select E.name, B.bonus
  from Employee E
  left outer join Bonus B
  on E.empId = B.empId
  where B.bonus < 1000 or B.bonus is null
-- @lc code=end

