"""
27.移除元素
https://leetcode.cn/problems/remove-element/
给你一个数组nums和一个值val，你需要原地移除所有数值等于val的元素，
并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用O(1)额外空间并原地修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

B站：https://www.bilibili.com/video/BV12A4y1Z7LP
代码随想录：https://programmercarl.com/0027.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.html
"""
from typing import List

# 双指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow
