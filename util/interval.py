# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    @staticmethod
    def generate_intervals(nums):
        result = []
        for pair in nums:
            tmp = Interval(pair[0], pair[1])
            result.append(tmp)
        return result

    @staticmethod
    def generate_list(intervals):
        result = []
        for inv in intervals:
            tmp = [inv.start, inv.end]
            result.append(tmp)
        return result