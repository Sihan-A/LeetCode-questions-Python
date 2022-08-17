"""
70.爬楼梯
https://leetcode.cn/problems/climbing-stairs/
假设你正在爬楼梯。需要n阶你才能到达楼顶。
每次你可以爬1或2个台阶。你有多少种不同的方法可以爬到楼顶呢？
dp[n]：n阶所需方法数
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]
        if n <= 2:
            return dp[n]
        
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2])
        
        return dp[n]
