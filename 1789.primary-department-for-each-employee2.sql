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
UNION
SELECT
  employee_id,
  max(department_id) department_id
from
  Employee
GROUP BY employee_id
having count(*) = 1

-- @lc code=end
