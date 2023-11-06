--
-- @lc app=leetcode id=1164 lang=mysql
--
-- [1164] Product Price at a Given Date
--

-- @lc code=start
# Write your MySQL query statement below
SELECT
  P1.product_id,
  P1.new_price price,
  P2.product_id
  from Products P1
  left outer join (
    select *
      from Products
      where change_date <= '2019-08-16'
  ) P2
  on P1.product_id = P2.product_id
-- @lc code=end

