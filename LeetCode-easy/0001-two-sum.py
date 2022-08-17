"""
1.两数之和
https://leetcode.cn/problems/two-sum/
给定一个整数数组nums和一个整数目标值target，
请你在该数组中找出和为目标值target的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。
但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
"""
from typing import List

# 方法1: 哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for idx, val in enumerate(nums):
            if target - val not in hashmap:
                hashmap[val] = idx
            else:
                return [hashmap[target - val], idx]

# 方法2: 遍历（很慢）
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
