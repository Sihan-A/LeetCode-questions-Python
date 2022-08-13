/*
1965.丢失信息的雇员
https://leetcode.cn/problems/employees-with-missing-information/
写出一个查询语句，找到所有丢失信息的雇员id。
当满足下面一个条件时，就被认为是雇员的信息丢失：
雇员的姓名丢失了，或者
雇员的薪水信息丢失了，或者
返回这些雇员的id：employee_id，从小到大排序。
*/

-- https://www.cnblogs.com/littlemonsterksn/p/16274736.html

SELECT e.employee_id
FROM employees AS e LEFT OUTER JOIN salaries AS s
on e.employee_id = s.employee_id
where s.salary IS NULL

UNION

SELECT s.employee_id
FROM employees AS e RIGHT OUTER JOIN salaries AS s
ON e.employee_id = s.employee_id
WHERE e.name IS NULL

ORDER BY employee_id;

