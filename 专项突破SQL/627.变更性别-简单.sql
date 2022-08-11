/*
627.变更性别
https://leetcode.cn/problems/swap-salary/
请你编写一个SQL查询来交换所有的'f'和'm'（即，将所有'f'变为'm'，反之亦然），
仅使用单个update语句，且不产生中间临时表。
注意，你必须仅使用一条update语句，且不能使用select语句。
*/
UPDATE salary
SET
sex = CASE sex
    WHEN 'm' THEN 'f'
    WHEN 'f' THEN 'm' -- ELSE 'm'
END;