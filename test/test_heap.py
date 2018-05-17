import heapq
import functools

arr = []

a = (1, 2, 'a')
b = (1, 3, 'b')
c = (5, 0, 'c')

arr.append(c)
arr.append(b)
arr.append(a)

print(arr)

heapq.heapify(arr)
print(arr)

arr = ['c', 'cd', 'a', 'b']
print(arr)
heapq.heapify(arr)
print(arr)

@functools.total_ordering
class MyCell:
    def __init__(self, x, y):
        self._data = {
            "x": x,
            "y": y
        }
        # self._data["x"] = x
        # self._data["y"] = y

    def __lt__(self, other):
        return self._data["y"] > other.y if self._data["x"] == other.x else self._data["x"] < other.x


    def __eq__(self, other):
        return self._data["x"] == other.x and self._data["y"] == other.y

    def __repr__(self):
        return repr((self._data["x"], self._data["y"]))

    @property
    def x(self):
        return self._data["x"]

    @x.setter
    def x(self, value):
        self._data["x"] = value

    @x.deleter
    def x(self):
        print("deleter of x called")
        del self._data["x"]

    @property
    def y(self):
        return self._data["y"]

    @y.setter
    def y(self, value):
        self._data["y"] = value


a = MyCell(1, 2)
b = MyCell(1, 5)
c = MyCell(3, 4)
d = MyCell(5, 6)

arr = [d, c, b, a]
print(arr)
heapq.heapify(arr)
print(arr)