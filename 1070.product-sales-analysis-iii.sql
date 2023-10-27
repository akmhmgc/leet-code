--
-- @lc app=leetcode id=1070 lang=mysql
--
-- [1070] Product Sales Analysis III
--

-- @lc code=start
# Write your MySQL query statement below
SELECT
  S.product_id,
  S.year first_year,
  S.quantity,
  S.price
  from Sales S
  where (S.product_id, S.year) in (
    select product_id, min(year)
      from Sales
      GROUP BY product_id
  )
-- @lc code=end

