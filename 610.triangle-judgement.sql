--
-- @lc app=leetcode id=610 lang=mysql
--
-- [610] Triangle Judgement
--

-- @lc code=start
# Write your MySQL query statement below
# Write your MySQL query statement below

select
  x,y,z,
  case
    when x >= y and x >= z then (
      case
        when  x < y + z then 'Yes'
        else 'No'
      end
    )
    when y >= x and y >= z then (
      case
        when  y < x + z then 'Yes'
        else 'No'
      end
    )
    else (
      case
        when  z < x + y then 'Yes'
        else 'No'
      end
    )
  end triangle
  from Triangle
-- @lc code=end

