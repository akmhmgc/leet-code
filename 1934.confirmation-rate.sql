--
-- @lc app=leetcode id=1934 lang=mysql
--
-- [1934] Confirmation Rate
--

-- @lc code=start
# Write your MySQL query statement belows

select
  S.user_id,
  round(
    sum(
      case
        when C.action = 'confirmed' then 1
        else 0
      end
    ) / count(*)
  , 2) confirmation_rate
  from Signups S
  left outer join Confirmations C
  on S.user_id = C.user_id
  group by S.user_id

-- @lc code=end

