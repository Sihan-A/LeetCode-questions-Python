"""
383.赎金信
https://leetcode.cn/problems/ransom-note/
给你两个字符串：ransomNote和magazine，
判断ransomNote能不能由magazine里面的字符构成。
如果可以，返回true；否则返回false。
magazine中的每个字符只能在ransomNote中使用一次。
"""
import collections

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if set(ransomNote) > set(magazine):
            return False
        
        magazine_count = collections.Counter(magazine)
        ransomNote_count = collections.Counter(ransomNote)

        for i, j in ransomNote_count.items():
            if j > magazine_count[i]:
                return False
        
        return True
