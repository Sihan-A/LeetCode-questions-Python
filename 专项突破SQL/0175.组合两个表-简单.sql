/*
175.组合两个表
https://leetcode.cn/problems/combine-two-tables/
编写一个SQL查询来报告Person表中每个人的姓、名、城市和州。 -> row 8
如果personId的地址不在Address表中，则报告为空null。-> row 9
以任意顺序返回结果表。
*/
SELECT LastName, FirstName, City, State
FROM Person LEFT JOIN Address
ON Person.PersonId = Address.PersonId;
