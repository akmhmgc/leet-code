--
-- @lc app=leetcode id=550 lang=mysql
--
-- [550] Game Play Analysis IV
--
-- @lc code=start
# Write your MySQL query statement below
SELECT
  round(count(distinct(A1.player_id)) / (
    select count(distinct(A3.player_id))
    from Activity A3
  ), 2) fraction
from
  Activity A1
where
  EXISTS (
    select
      *
    from
      Activity A2
    where
      A2.player_id = A1.player_id
    group by A2.player_id
    HAVING min(A2.event_date) = DATE_SUB(A1.event_date, INTERVAL 1 DAY)
  )

-- @lc code=end
