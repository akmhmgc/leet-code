--
-- @lc app=leetcode id=1280 lang=mysql
--
-- [1280] Students and Examinations
--

-- @lc code=start
# Write your MySQL query statement below

select
  St.student_id,
  St.student_name,
  Sb.subject_name,
  (
    select count(*)
      from Examinations E
      where E.student_id = St.student_id
      and E.subject_name = Sb.subject_name
  ) attended_exams
from Students St, Subjects Sb
order by St.student_id, Sb.subject_name

-- @lc code=end

