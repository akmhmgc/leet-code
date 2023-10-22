--
-- @lc app=leetcode id=1193 lang=mysql
--
-- [1193] Monthly Transactions I
--
-- @lc code=start
# Write your MySQL query statement below
select
  date_format(trans_date, '%Y-%m') month,
  country,
  count(*) trans_count,
  sum(
    case
      when state = 'approved' then 1
      else 0
    end
  ) approved_count,
  sum(amount) trans_total_amount,
  sum(
    amount * (
      case
        when state = 'approved' then 1
        else 0
      end
    )
  ) approved_total_amount
from
  Transactions
GROUP BY
  country, date_format(trans_date, '%Y-%m')

-- @lc code=end
