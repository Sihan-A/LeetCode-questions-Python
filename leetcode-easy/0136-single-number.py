"""
0136.只出现一次的数字
https://leetcode.cn/problems/single-number/
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
找出那个只出现了一次的元素。
"""
from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for key, value in Counter(nums).items():
            if value == 1:
                return key
