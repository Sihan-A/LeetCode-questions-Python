"""
977.有序数组的平方
https://leetcode.cn/problems/squares-of-a-sorted-array/
给你一个按非递减顺序排序的整数数组nums，
返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
https://programmercarl.com/0977.%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E7%9A%84%E5%B9%B3%E6%96%B9.html#%E6%9A%B4%E5%8A%9B%E6%8E%92%E5%BA%8F
"""
# 方法1: 暴力
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_square = [i**2 for i in nums]
        nums_square.sort()
        return nums_square

# 方法2: 双指针
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j, k = 0, len(nums)-1, len(nums)-1
        result = [0 for _ in range(len(nums))]

        while i <= j:
            if abs(nums[i]) <= abs(nums[j]):
                result[k] = nums[j] ** 2
                j -= 1
            else:
                result[k] = nums[i] ** 2
                i += 1
            k -= 1
        
        return result