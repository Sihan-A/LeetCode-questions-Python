/*
584.寻找用户推荐人
https://leetcode.cn/problems/find-customer-referee/
写一个查询语句，返回一个客户列表，列表中客户的推荐人的编号都不是2。
*/
SELECT name FROM customer
WHERE referee_id <> 2 OR referee_id IS NULL
