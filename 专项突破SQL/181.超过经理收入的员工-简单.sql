/*
181.超过经理收入的员工
https://leetcode.cn/problems/employees-earning-more-than-their-managers/
编写一个SQL查询来查找收入比经理高的员工。
以任意顺序返回结果表。
*/

SELECT a.name as Employee
FROM Employee a, Employee b
WHERE 
    a.managerId = b.id -- Joe的领导是Sam
    AND 
    a.salary > b.salary

/*
输入:
Employee表:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
输出:
+----------+
| Employee |
+----------+
| Joe      |
+----------+
解释:Joe是唯一挣得比经理多的雇员。
*/