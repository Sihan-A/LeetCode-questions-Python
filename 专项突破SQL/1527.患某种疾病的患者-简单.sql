/*
1527.患某种疾病的患者
https://leetcode.cn/problems/patients-with-a-condition/
写一条SQL语句，查询患有I类糖尿病的患者ID（patient_id）、患者姓名（patient_name）以及其患有的所有疾病代码（conditions）。
I类糖尿病的代码总是包含前缀DIAB1。
按任意顺序返回结果表。
*/
SELECT
    patient_id, patient_name, conditions
FROM
    Patients
WHERE 
    conditions LIKE 'DIAB1%' 
        OR 
    conditions LIKE '% DIAB1%'
