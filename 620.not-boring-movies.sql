--
-- @lc app=leetcode id=620 lang=mysql
--
-- [620] Not Boring Movies
--

-- @lc code=start
# Write your MySQL query statement below
SELECT id, movie, description, rating
  from Cinema
  where MOD(id, 2) = 1
  and description != 'boring'
  ORDER BY rating desc
-- @lc code=end

