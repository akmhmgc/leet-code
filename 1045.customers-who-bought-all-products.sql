--
-- @lc app=leetcode id=1045 lang=mysql
--
-- [1045] Customers Who Bought All Products
--

-- @lc code=start
# Write your MySQL query statement below
SELECT
  C.customer_id
  from Customer C
  inner join Product P
  on C.product_key = P.product_key
  group by C.customer_id
  having count(distinct(C.product_key)) = (
    select count(*)
      from Product
  )
-- @lc code=end

