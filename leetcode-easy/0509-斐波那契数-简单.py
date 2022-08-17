"""
https://leetcode.cn/problems/fibonacci-number/
斐波那契数（通常用F(n)表示）形成的序列称为斐波那契数列。
该数列由0和1开始，后面的每一项数字都是前面两项数字的和。也就是：
F(0) = 0，F(1)= 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定n，请计算F(n)。
"""

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        dp = [0] * (n+1)
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
