/*
196.删除重复的电子邮箱
https://leetcode.cn/problems/delete-duplicate-emails/
编写一个SQL删除语句来删除所有重复的电子邮件，只保留一个id最小的唯一电子邮件。
以任意顺序返回结果表。
（注意：仅需要写删除语句，将自动对剩余结果进行查询）
*/

DELETE p1
FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND p1.Id > p2.Id
