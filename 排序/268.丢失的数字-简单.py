"""
268.丢失的数字
https://leetcode.cn/problems/missing-number/
给定一个包含[0, n]中n个数的数组nums，
找出[0, n]这个范围内没有出现在数组中的那个数。
"""
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums_full = {i for i in range(len(nums)+1)}
        nums_set = set(nums)
        return (nums_full - nums_set).pop()
