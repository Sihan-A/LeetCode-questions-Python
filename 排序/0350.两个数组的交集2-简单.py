"""
350.两个数组的交集2
https://leetcode.cn/problems/intersection-of-two-arrays-ii/
给你两个整数数组 nums1和nums2，请你以数组形式返回两数组的交集。
返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。
可以不考虑输出结果的顺序。
"""
from typing import List

# 方法1: 先找出并集，再统计最小出现数
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        intersection = list(set(nums1) & set(nums2))
        for i in intersection:
            temp = [i] * min(nums1.count(i), nums2.count(i))
            result.extend(temp)
        return result

