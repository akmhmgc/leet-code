--
-- @lc app=leetcode id=602 lang=mysql
--
-- [602] Friend Requests II: Who Has the Most Friends
--
-- @lc code=start
# Write your MySQL query statement below
select
  id,
  count(*) num
from
  (
    select
      requester_id id
    from
      RequestAccepted
    union
    all
    select
      accepter_id id
    from
      RequestAccepted
  ) tmp
  group by id
  order by num desc
  limit 1
-- @lc code=end
