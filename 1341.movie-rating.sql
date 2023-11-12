--
-- @lc app=leetcode id=1341 lang=mysql
--
-- [1341] Movie Rating
--
-- @lc code=start
# Write your MySQL query statement below
(
  select
    u.name results
  from
    MovieRating
    inner join Users u using(user_id)
  GROUP BY
    u.name
  order by
    count(*) desc,
    results asc
  limit
    1
)
UNION
(
  select
    m.title results
  from
    MovieRating mr
    inner join Movies m using(movie_id)
  where
    mr.created_at between '2020-02-01'
    and '2020-02-28'
  GROUP BY
    m.title
  order by
    avg(mr.rating) desc,
    results asc
  limit
    1
)
-- @lc code=end
