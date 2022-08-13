"""
252.会议室
https://leetcode.cn/problems/meeting-rooms
给定一个会议时间安排的数组intervals，
每个会议时间都会包括开始和结束的时间intervals[i] = [starti, endi]，
请你判断一个人是否能够参加这里面的全部会议。
"""

from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort(key=lambda x:x[0]) # 根据开始时间排序列表
        
        if len(intervals) <= 1: # 后面有i-1的操作，先把这一步做了
            return True
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
