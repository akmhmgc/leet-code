--
-- @lc app=leetcode id=1581 lang=mysql
--
-- [1581] Customer Who Visited but Did Not Make Any Transactions
--

-- @lc code=start
# Write your MySQL query statement below
select 
  V.customer_id customer_id,
  count(*) count_no_trans
  from Visits V
  left outer join Transactions T
  on V.visit_id = T.visit_id
  where T.transaction_id is null
  group by V.customer_id
  

-- @lc code=end

