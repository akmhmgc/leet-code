--
-- @lc app=leetcode id=1321 lang=mysql
--
-- [1321] Restaurant Growth
--
-- @lc code=start
# Write your MySQL query statement below
select
  visited_on,
  amount,
  round(amount / 7, 2) average_amount
from
  (
    select
      distinct visited_on,
      sum(amount) over (
        order by
          visited_on asc range between interval '6' day preceding
          and current row
      ) amount,
      min(visited_on) over () min_visited_on
    from
      Customer
  ) tmp
where
  tmp.visited_on >= tmp.min_visited_on + 6

-- @lc code=end
