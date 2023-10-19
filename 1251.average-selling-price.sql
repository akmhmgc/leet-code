--
-- @lc app=leetcode id=1251 lang=mysql
--
-- [1251] Average Selling Price
--
-- @lc code=start
# Write your MySQL query statement below
select
  P.product_id,
  IFNULL(
    round(sum(P.price * us.units) / sum(us.units), 2),
    0
  ) average_price
from
  Prices P
  left outer join UnitsSold US on P.product_id = US.product_id
  and us.purchase_date BETWEEN p.start_date
  and p.end_date
group by
  P.product_id

-- @lc code=end
