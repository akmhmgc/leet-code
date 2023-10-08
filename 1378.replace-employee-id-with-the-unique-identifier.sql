--
-- @lc app=leetcode id=1378 lang=mysql
--
-- [1378] Replace Employee ID With The Unique Identifier
--

-- @lc code=start
# Write your MySQL query statement below
select u.unique_id, e.name
  from Employees e
  left outer join EmployeeUNI u
  on e.id = u.id

-- @lc code=end

