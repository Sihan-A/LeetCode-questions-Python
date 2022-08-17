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

#方法2: 二分法 2022.08.17
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        # 如果target在nums里，二分法找到
        while left <= right:
            middle = (left+right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        
        # 如果target不在nums里
        if nums[middle] > target:
            return middle
        else:
            return middle + 1
