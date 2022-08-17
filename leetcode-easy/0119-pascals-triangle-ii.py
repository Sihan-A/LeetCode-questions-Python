"""
https://leetcode.cn/problems/pascals-triangle-ii/
给定一个非负索引rowIndex，返回「杨辉三角」的第rowIndex行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
"""

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowNum = rowIndex + 1
        dp = [[0] * i for i in range(1, rowNum+1)]

        for i in range(rowNum):
            dp[i][0], dp[i][i] = 1,1
            for j in range(1, i):
                dp[i][j]=dp[i-1][j] + dp[i-1][j-1]
        
        return dp[rowIndex]
