--
-- @lc app=leetcode id=1070 lang=mysql
--
-- [1070] Product Sales Analysis III
--
-- @lc code=start
# Write your MySQL query statement below
SELECT
  S1.product_id,
  S1.year first_year,
  S1.quantity,
  S1.price
from
  Sales S1
  inner join (
    select
      product_id,
      min(year) min_year
    from
      Sales
    GROUP BY
      product_id
  ) tmp on S1.product_id = tmp.product_id
  and S1.year = tmp.min_year
  
-- @lc code=end
