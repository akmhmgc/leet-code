--
-- @lc app=leetcode id=1321 lang=mysql
--
-- [1321] Restaurant Growth
--
-- @lc code=start
# Write your MySQL query statement below
select
  visited_on,
  sum(amount) over (
    order by
      visited_on asc range between interval '6' day preceding
      and current row
  ) amount,
  round(
    avg(amount) over (
      order by
        visited_on asc range between interval '6' day preceding
        and current row
    ),
    2
  ) average_amount,
  min(visited_on) over (
  ) min_visited_on
from
  Customer

-- @lc code=end
