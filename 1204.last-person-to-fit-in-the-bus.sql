--
-- @lc app=leetcode id=1204 lang=mysql
--
-- [1204] Last Person to Fit in the Bus
--
-- @lc code=start
# Write your MySQL query statement belowselect
SELECT
  person_name
from
  (
    select
      person_name,
      sum(weight) over (
        ORDER BY
          turn
      ) sum_weight
    from
      Queue
  ) tmp
where
  tmp.sum_weight <= 1000
order by
  tmp.sum_weight desc
limit
  1

-- @lc code=end
