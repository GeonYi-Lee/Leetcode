# Write your MySQL query statement below
select A.firstName, A.lastName, B.city, B.state
from person A
left join address B on A.personid = B.personid