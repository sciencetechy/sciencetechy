"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

class Solution:
    def merge(self, intervals):
        intervals.sort()
        final = []

        for i in intervals:
            if not final or final[-1][1] < i[0]:
                final.append(i)
            else:
                final[-1][1] = max(final[-1][1], i[1])
        
        return final