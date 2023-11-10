--
-- @lc app=leetcode id=1978 lang=mysql
--
-- [1978] Employees Whose Manager Left the Company
--
-- @lc code=start
# Write your MySQL query statement belowse
select
  employee_id
from
  Employees E1
where
  salary < 30000
  and manager_id is not null
  and not exists (
    select
      *
    from
      Employees E2
    where
      E2.employee_id = E1.manager_id
  )
order by
  employee_id

-- @lc code=end
