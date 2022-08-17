"""
704.二分查找
https://leetcode.cn/problems/binary-search
给定一个n个元素有序的（升序）整型数组nums和一个目标值target，
写一个函数搜索nums中的target，
如果目标值存在返回下标，否则返回-1。
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            middle = (left + right) // 2 # median
            
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else: # equal
                return middle

        return -1
