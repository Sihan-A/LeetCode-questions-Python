/*
1757.可回收且低脂的产品
https://leetcode.cn/problems/recyclable-and-low-fat-products/
写出SQL语句，查找既是低脂又是可回收的产品编号。
返回结果无顺序要求。
*/

SELECT product_id FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y'
