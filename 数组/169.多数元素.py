import collections
from typing import List

"""
https://leetcode.cn/problems/majority-element/
给定一个大小为n的数组nums，返回其中的多数元素。
多数元素是指在数组中出现次数大于⌊n/2⌋的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""

# 计数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for key, value in collections.Counter(nums).items():
            if value > (len(nums) / 2):
                return key

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# 现排序，再找中位数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
