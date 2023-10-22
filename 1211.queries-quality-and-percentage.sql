--
-- @lc app=leetcode id=1211 lang=mysql
--
-- [1211] Queries Quality and Percentage
--
-- @lc code=start
# Write your MySQL query statement below
select
  query_name,
  round(avg(rating / position), 2) quality,
  round(
    avg(
      case
        when rating < 3 then 1
        else 0
      end
    ) * 100,
    2
  ) poor_query_percentage
from
  Queries
GROUP BY
  query_name
-- @lc code=end
