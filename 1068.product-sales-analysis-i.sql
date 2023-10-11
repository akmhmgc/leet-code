--
-- @lc app=leetcode id=1068 lang=mysql
--
-- [1068] Product Sales Analysis I
--

-- @lc code=start
# Write your MySQL query statement below
select product_name, year, price
  from Product P
  inner join Sales S
  on P.product_id = S.product_id

-- @lc code=end

