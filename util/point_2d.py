# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


    @staticmethod
    def get_points_from_array(nums):
        res = []
        if not nums:
            return res
        for num in nums:
            p = Point(num[0], num[1])
            res.append(p)
        return res