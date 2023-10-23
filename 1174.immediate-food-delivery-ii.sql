--
-- @lc app=leetcode id=1174 lang=mysql
--
-- [1174] Immediate Food Delivery II
--

-- @lc code=start
# Write your MySQL query statement below
select
  round(avg(case
    when D1.order_date = D1.customer_pref_delivery_date then 1
    else 0
  end) * 100, 2) immediate_percentage
  from Delivery D1
  where not exists (
    select
      D2.order_date
      from Delivery D2
      where D2.customer_id = D1.customer_id
      and D2.order_date < D1.order_date
  )
-- @lc code=end

