"""
https://leetcode.cn/problems/min-cost-climbing-stairs/
给你一个整数数组cost，其中cost[i]是从楼梯第i个台阶向上爬需要支付的费用。
一旦你支付此费用，即可选择向上爬一个或者两个台阶。
你可以选择从下标为0或下标为1的台阶开始爬楼梯。
请你计算并返回达到楼梯顶部的最低花费。

代码随想录：https://programmercarl.com/0746.%E4%BD%BF%E7%94%A8%E6%9C%80%E5%B0%8F%E8%8A%B1%E8%B4%B9%E7%88%AC%E6%A5%BC%E6%A2%AF.html#
"""
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) <= 2: # 后面有i-2的操作
            return min(cost)
        
        # dp init
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        return min(dp[-1], dp[-2])
