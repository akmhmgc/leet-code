--
-- @lc app=leetcode id=585 lang=mysql
--
-- [585] Investments in 2016
--

-- @lc code=start
# Write your MySQL query statement below
SELECT
  round(sum(I1.tiv_2016), 2) tiv_2016
  from Insurance I1
  where EXISTS (
    SELECT *
      from Insurance I2
      where I2.pid != I1.pid
      and I2.tiv_2015 = I1.tiv_2015
  ) and not EXISTS (
    SELECT *
      from Insurance I3
      where I3.pid != I1.pid
      and (I3.lat, I3.lon) in (I1.lat, I1.lon)
  )
-- @lc code=end

