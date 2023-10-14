--
-- @lc app=leetcode id=197 lang=mysql
--
-- [197] Rising Temperature
--

-- @lc code=start
# Write your MySQL query statement below
select id
  from (
    select
    id,
    temperature,
    max(temperature) over (order by recordDate asc range BETWEEN INTERVAL 1 DAY preceding and INTERVAL 1 DAY preceding) pre_temperature
    from Weather
  ) tmp
  where tmp.temperature > tmp.pre_temperature

-- @lc code=end

