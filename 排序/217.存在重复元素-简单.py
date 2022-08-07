"""
217.存在重复元素
https://leetcode.cn/problems/contains-duplicate/
给你一个整数数组nums。
如果任一值在数组中出现至少两次，返回true；
如果数组中每个元素互不相同，返回false。
"""
from typing import List

# 方法1: 集合
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        return len(nums) != len(set_nums)

# 方法2: 遍历列表加元素到集合，碰到重复的就返回 True，没有就继续加
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temporary_set = set()
        
        for i in nums:
            if i in temporary_set:
                return True
            else:
                temporary_set.add(i)
        
        return False
        