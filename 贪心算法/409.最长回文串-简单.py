"""
409.最长回文串
https://leetcode.cn/problems/longest-palindrome/
给定一个包含大写字母和小写字母的字符串s，返回通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。
比如"Aa"不能当做一个回文字符串。
"""
import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        odd = 0
        counter = collections.Counter(s)
        
        for value in counter.values():
            result += (value//2) * 2
            if odd == 0 and value%2 != 0:
                odd = 1
                
        result += odd
        return result

