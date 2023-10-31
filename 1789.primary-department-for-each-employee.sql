--
-- @lc app=leetcode id=1789 lang=mysql
--
-- [1789] Primary Department for Each Employee
--
-- @lc code=start
# Write your MySQL query statement below
SELECT
  E1.employee_id,
  E1.department_id
from
  Employee E1
where E1.primary_flag = 'Y'
or (
  SELECT
    count(*)
    from Employee E2
    where E2.employee_id = E1.employee_id
) = 1

-- @lc code=end
