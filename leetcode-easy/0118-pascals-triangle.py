"""
https://leetcode.cn/problems/pascals-triangle/
给定一个非负整数numRows，生成「杨辉三角」的前numRows行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1] * i for i in range(1, numRows+1)] # init dp
        
        if numRows <= 2:
            return dp
        
        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] # 动态方程
        
        return dp