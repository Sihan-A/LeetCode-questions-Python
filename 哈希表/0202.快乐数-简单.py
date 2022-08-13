"""
202.快乐数
https://leetcode.cn/problems/happy-number/
编写一个算法来判断一个数n是不是快乐数。
「快乐数」定义为：
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为1，也可能是无限循环但始终变不到1。
如果这个过程结果为1，那么这个数就是快乐数。
如果n是快乐数就返回true；不是，则返回false。

讲解：代码随想录
当我们遇到了要快速判断一个元素是否出现集合里的时候，就要考虑哈希法了。
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        result = self.calculate_sum(n)

        while result != 1:
            if result in record:
                return False
            else:
                record.add(result)
                result = self.calculate_sum(result)
        
        return True

    def calculate_sum(self, n):
        # 19: 1^2 + 9^2 = 82
        sum = 0
        for i in range(len(str(n))):
            sum += int(str(n)[i]) ** 2
        return sum
