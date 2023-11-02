--
-- @lc app=leetcode id=1164 lang=mysql
--
-- [1164] Product Price at a Given Date
--

-- @lc code=start
# Write your MySQL query statement below
SELECT
  DISTINCT(product_id),
  10 price
  from Products
except
SELECT
  DISTINCT(product_id),
  10 price
  from Products
  where change_date <= '2019-08-16'
UNION
SELECT
  P1.product_id,
  P1.new_price price
  from Products P1
  where P1.change_date <= '2019-08-16'
  and not EXISTS (
    select
      *
      from Products P2
      where P2.product_id = P1.product_id
      and P2.change_date <= '2019-08-16'
      and P2.change_date > P1.change_date
  )
-- @lc code=end

