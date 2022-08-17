"""
349.两个数组的交集
https://leetcode.cn/problems/intersection-of-two-arrays/
给定两个数组nums1和nums2，返回它们的交集。
输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。
"""
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))