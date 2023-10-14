--
-- @lc app=leetcode id=1661 lang=mysql
--
-- [1661] Average Time of Process per Machine
--
-- @lc code=start
# Write your MySQL query statement below
select
  machine_id,
  round(avg(diff),3) processing_time
from
  (
    select
      machine_id,
      process_id,
      max(timestamp) - min(timestamp) as diff
    from
      Activity
    group by
      machine_id,
      process_id
  ) tmp
  group by tmp.machine_id
  
-- @lc code=end
