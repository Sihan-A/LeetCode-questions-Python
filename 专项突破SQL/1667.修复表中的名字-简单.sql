/*
1667.修复表中的名字
https://leetcode.cn/problems/fix-names-in-a-table/
编写一个SQL查询来修复名字，使得只有第一个字符是大写的，其余都是小写的。
返回按user_id排序的结果表。
*/

SELECT
    user_id,
    CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTR(name, 2))) as name
FROM Users
ORDER BY user_id
