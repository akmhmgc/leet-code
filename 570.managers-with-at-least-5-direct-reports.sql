--
-- @lc app=leetcode id=570 lang=mysql
--
-- [570] Managers with at Least 5 Direct Reports
--

-- @lc code=start
# Write your MySQL query statement below

select E2.name
  from Employee E1
  inner join Employee E2
  on E1.managerId = E2.id
  group by E2.id, E2.name
  having count(*) >= 5

-- @lc code=end

