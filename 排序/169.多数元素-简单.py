"""
https://leetcode.cn/problems/majority-element/
给定一个大小为 n 的数组 nums ，返回其中的多数元素。
多数元素是指在数组中出现次数大于⌊n/2⌋的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""
from typing import List
import collections

# 方法1: 计数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# 方法2: 中位数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
