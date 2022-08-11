/*
1873.计算特殊奖金
https://leetcode.cn/problems/calculate-special-bonus/
写出一个SQL查询语句，计算每个雇员的奖金。
如果一个雇员的id是奇数并且他的名字不是以'M'开头，
那么他的奖金是他工资的100%，否则奖金为0。
返回的结果集请按照employee_id排序。
*/

SELECT
    employee_id,
    (CASE
        WHEN (name NOT LIKE "M%" and MOD(employee_id,2)=1) THEN salary
        ELSE 0
    END) AS bonus
FROM Employees
ORDER BY employee_id
