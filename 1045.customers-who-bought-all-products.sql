--
-- @lc app=leetcode id=1045 lang=mysql
--
-- [1045] Customers Who Bought All Products
--

-- @lc code=start
# Write your MySQL query statement below
SELECT
  customer_id
  from Customer
  group by customer_id
  having count(distinct(product_key)) = (
    select count(*)
      from Product
  )
-- @lc code=end

