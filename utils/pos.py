from typing import NamedTuple


class Pos(NamedTuple("Pos", [("x", int), ("y", int)])):
    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

    def __mul__(self, num):
        return Pos(self.x * num, self.y * num)

    __rmul__ = __mul__

    def dist(self, other) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    @property
    def near4(self):
        return [
            self + Pos(i, j)
            for i in [-1, 0, 1]
            for j in [-1, 0, 1]
            if (i == 0) ^ (j == 0)
        ]

    @property
    def near8(self):
        return [
            self + Pos(i, j)
            for i in [-1, 0, 1]
            for j in [-1, 0, 1]
            if (i != 0) or (j != 0)
        ]
