"""
454.四数相加II
https://leetcode.cn/problems/4sum-ii
给你四个整数数组nums1、nums2、nums3和nums4，数组长度都是n，
请你计算有多少个元组(i,j,k,l)能满足：
0<=i,j,k,l<n
nums1[i]+nums2[j]+nums3[k]+nums4[l]==0
"""
from typing import List
# 方法1: 分组+哈希表
class Solution:
    def fourSumCount(self, nums1: List[int],nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap_AB = dict()
        for i in nums1:
            for j in nums2:
                if i+j in hashmap_AB:
                    hashmap_AB[i+j] += 1
                else:
                    hashmap_AB[i+j] = 1
        result = 0
        for k in nums3:
            for l in nums4:
                if -(k+l) in hashmap_AB:
                    result += hashmap_AB[-(k+l)]
        
        return result
