--
-- @lc app=leetcode id=1321 lang=mysql
--
-- [1321] Restaurant Growth
--
-- @lc code=start
# Write your MySQL query statement below
select
  tmp2.visited_on,
  tmp2.amount,
  tmp2.average_amount
from
  (
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
      count(amount) over (
        order by
          visited_on asc range between interval '6' day preceding
          and current row
      ) cnt
    from
      (
        select
          visited_on,
          sum(amount) amount
        from
          Customer
        group by
          visited_on
        order by
          visited_on
      ) tmp
  ) tmp2
  where tmp2.cnt = 7

-- @lc code=end
