"""
242.有效的字母异位词
https://leetcode.cn/problems/valid-anagram/
给定两个字符串s和t，编写一个函数来判断t是否是s的字母异位词。
注意：若s和t中每个字符出现的次数都相同，则称s和t互为字母异位词。
"""
# 方法1: 计数器
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

# 方法2: 哈希表 defaultdict
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i, j in zip(s, t):
            s_dict[i] += 1
            t_dict[j] += 1
        
        return s_dict == t_dict
