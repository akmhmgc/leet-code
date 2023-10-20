--
-- @lc app=leetcode id=1633 lang=mysql
--
-- [1633] Percentage of Users Attended a Contest
--
-- @lc code=start
# Write your MySQL query statement below
SELECT
  R.contest_id,
  round(
    count(*) * 100 / (
      select
        count(*)
      from
        Users
    ),
    2
  ) percentage 
  from Register R
  inner join Users U
  on R.user_id = U.user_id
  group by R.contest_id
  order by percentage desc, R.contest_id asc

-- @lc code=end
