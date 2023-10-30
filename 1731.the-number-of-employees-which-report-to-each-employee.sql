--
-- @lc app=leetcode id=1731 lang=mysql
--
-- [1731] The Number of Employees Which Report to Each Employee
--

-- @lc code=start
# Write your MySQL query statement below
select
  E1.employee_id,
  E1.name,
  count(*) reports_count,
  round(avg(E2.age),0) average_age
  from Employees E1
  inner join Employees E2
  on E1.employee_id = E2.reports_to
  group by E1.employee_id
  order by E1.employee_id

-- @lc code=end

