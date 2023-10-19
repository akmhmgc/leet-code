--
-- @lc app=leetcode id=1075 lang=mysql
--
-- [1075] Project Employees I
--
-- @lc code=start
# Write your MySQL query statement below
select
  p.project_id,
  round(avg(e.experience_years), 2) average_years
from
  Project p
  inner join Employee e
  on p.employee_id = e.employee_id
group by
  p.project_id

-- @lc code=end
