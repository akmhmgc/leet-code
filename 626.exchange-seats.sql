--
-- @lc app=leetcode id=626 lang=mysql
--
-- [626] Exchange Seats
--
-- @lc code=start
# Write your MySQL query statement below
select
  id,
  case
    when id % 2 = 0 then (
      lag(student) over (
        order by
          id
      )
    )
    else ifnull(
      lead(student) over (
        order by
          id
      ),
      student
    )
  END as "student"
from
  Seat

-- @lc code=end
