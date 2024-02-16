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
            if i**2 + j**2 == 1
        ]

    @property
    def near8(self):
        return [
            self + Pos(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)
        ]

    near_all = near8


class Pos3D(NamedTuple("Pos", [("x", int), ("y", int), ("z", int)])):
    def __add__(self, other):
        return Pos3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, num):
        return Pos3D(self.x * num, self.y * num, self.z * num)

    __rmul__ = __mul__

    @property
    def near6(self):
        return [
            self + Pos3D(i, j, k)
            for i in [-1, 0, 1]
            for j in [-1, 0, 1]
            for k in [-1, 0, 1]
            if i**2 + j**2 + k**2 == 1
        ]

    @property
    def near26(self):
        return [
            self + Pos3D(i, j, k)
            for i in [-1, 0, 1]
            for j in [-1, 0, 1]
            for k in [-1, 0, 1]
            if (i, j, k) != (0, 0, 0)
        ]

    near_all = near26


class Pos4D(NamedTuple("Pos", [("x", int), ("y", int), ("z", int), ("w", int)])):
    def __add__(self, other):
        return Pos4D(
            self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w
        )

    def __mul__(self, num):
        return Pos4D(self.x * num, self.y * num, self.z * num, self.w * num)

    __rmul__ = __mul__

    @property
    def near8(self):
        return [
            self + Pos4D(i, j, k, l)
            for i in [-1, 0, 1]
            for j in [-1, 0, 1]
            for k in [-1, 0, 1]
            for l in [-1, 0, 1]
            if i**2 + j**2 + k**2 + l**2 == 1
        ]

    @property
    def near80(self):
        return [
            self + Pos4D(i, j, k, l)
            for i in [-1, 0, 1]
            for j in [-1, 0, 1]
            for k in [-1, 0, 1]
            for l in [-1, 0, 1]
            if (i, j, k, l) != (0, 0, 0, 0)
        ]

    near_all = near80
