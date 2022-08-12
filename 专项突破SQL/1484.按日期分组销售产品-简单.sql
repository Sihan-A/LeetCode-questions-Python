/*
1484.按日期分组销售产品
https://leetcode.cn/problems/group-sold-products-by-the-date/
编写一个SQL查询来查找每个日期、销售的不同产品的数量及其名称。
每个日期的销售产品名称应按词典序排列。
返回按sell_date排序的结果表。
*/

SELECT
    sell_date,
    COUNT(DISTINCT product) num_sold,
    GROUP_CONCAT(DISTINCT product) products
FROM activities
GROUP BY sell_date
ORDER BY sell_date;
