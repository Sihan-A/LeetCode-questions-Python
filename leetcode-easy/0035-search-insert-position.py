"""
35.搜索插入位置
https://leetcode.cn/problems/search-insert-position/
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为O(logn)的算法。
"""
from typing import List

#方法1: 实在做不出来时候
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        return nums.index(target)

#方法2: 二分法
