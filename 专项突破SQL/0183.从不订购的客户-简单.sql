/*
183.从不订购的客户
https://leetcode.cn/problems/customers-who-never-order/
某网站包含两个表，Customers表和Orders表。
编写一个SQL查询，找出所有从不订购任何东西的客户。
*/
SELECT Customers.Name as 'Customers'
FROM customers
Where customers.Id not in (
    SELECT CustomerID FROM Orders
)
