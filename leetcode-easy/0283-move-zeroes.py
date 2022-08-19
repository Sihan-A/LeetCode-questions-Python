"""
283.移动零
https://leetcode.cn/problems/move-zeroes/
给定一个数组nums，编写一个函数将所有0移动到数组的末尾，
同时保持非零元素的相对顺序。
请注意，必须在不复制数组的情况下原地对数组进行操作。
"""
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right, left = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
            right += 1
