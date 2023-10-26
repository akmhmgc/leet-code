--
-- @lc app=leetcode id=1141 lang=mysql
--
-- [1141] User Activity for the Past 30 Days I
--

-- @lc code=start
# Write your MySQL query statement below
SELECT
  activity_date day,
  count(distinct(user_id)) active_users
  from Activity
  where activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) and '2019-07-27'
  GROUP BY activity_date
-- @lc code=end

