/*
595.大的国家
https://leetcode.cn/problems/big-countries/
如果一个国家满足下述两个条件之一，则认为该国是大国：
面积至少为300万平方公里（即，3000000 km2），或者
人口至少为2500万（即25000000）
编写一个SQL查询以报告大国的国家名称、人口和面积。
按任意顺序返回结果表。
*/

-- 方法1: WHERE 和 OR
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000

-- 方法2: Union
SELECT name, population, area FROM World
WHERE area >= 3000000

Union

SELECT name, population, area FROM World
WHERE population >= 25000000
