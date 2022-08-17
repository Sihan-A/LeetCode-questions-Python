"""
414.第三大的数
https://leetcode.cn/problems/third-maximum-number/
给你一个非空数组，返回此数组中第三大的数。
如果不存在，则返回数组中最大的数。
"""
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set_list = list(set(nums))
        if len(nums_set_list) < 3:
            return max(nums_set_list)
        
        nums_set_list.sort(reverse=True)
        return nums_set_list[2]
