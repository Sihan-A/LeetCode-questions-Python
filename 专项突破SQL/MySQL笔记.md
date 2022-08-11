MySQL笔记
===

1. 选择 `SELECT`

2. CASE语句

    ```mysql
    CASE
    	WHEN 条件1 THEN
    	WHEN 条件2 THEN
    	ELSE
    END CASE;
    ```

3. 计算

4. 求余

    - `MOD(column, 2) = 1`
    - `column % 2 = 1`

5. 联合

    - `inner join`：2表值都存在
    - `outer join`：附表中值可能存在null的情况。
    - 总结：
        1. `A inner join B`：取交集
        2. `A left join B`：取A全部，B没有对应的值，则为null
        3. `A right join B`：取B全部，A没有对应的值，则为null
        4. `A full outer join B`：取并集，彼此没有对应的值为null

    上述4种的对应条件，在`on`后填写。



