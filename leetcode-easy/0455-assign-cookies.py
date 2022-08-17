"""
455.分发饼干
标签：贪心、数组、排序
https://leetcode.cn/problems/assign-cookies/
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。
但是，每个孩子最多只能给一块饼干。
对每个孩子i，都有一个胃口值g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；
并且每块饼干j，都有一个尺寸s[j]。
如果s[j]>=g[i]，我们可以将这个饼干j分配给孩子i，这个孩子会得到满足。
你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
"""
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result = 0
        i = 0
        
        for j in range(len(s)):
            if i < len(g) and s[j] >= g[i]:
                result += 1
                i += 1
        return result
