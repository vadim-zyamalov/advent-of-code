from typing import NamedTuple
from dataclasses import dataclass
import heapq as hq
import time


class ElfRIP(Exception):
    pass


class Pos(NamedTuple("Pos", [("x", int), ("y", int)])):
    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)

    @property
    def near(self):
        return [
            self + d for d in [Pos(-1, 0), Pos(0, -1), Pos(0, 1), Pos(1, 0)]
        ]


@dataclass
class Unit:
    elf: bool
    pos: Pos
    hp: int = 200
    power: int = 3
    dead: bool = False

    def __repr__(self):
        return f"{'E' if self.elf else 'G'}:{self.hp}:{self.pos}"


class Cave:
    def __init__(self, lines: list[str], elf_power: int = 3) -> None:
        self.tiles = set()
        self.units = []

        for i, row in enumerate(lines):
            for j, el in enumerate(row):
                if el == "#":
                    continue
                self.tiles.add(Pos(i, j))
                if el in "EG":
                    self.units.append(
                        Unit(
                            el == "E",
                            Pos(i, j),
                            power=elf_power if el == "E" else 3,
                        )
                    )

    def __repr__(self):
        result = [u.__repr__() for u in self.units if not u.dead]
        return "[" + ", ".join(result) + "]"

    def move(self, beg: Unit, fins: list[Unit]) -> Pos | None:
        beg_pos = beg.pos
        fins_pos = []
        for u in fins:
            fins_pos.extend(u.pos.near)
        occupied = [u.pos for u in self.units if not u.dead and u != beg]
        fins_pos = [
            p for p in fins_pos if p not in occupied and p in self.tiles
        ]

        queue: list[tuple[int, Pos, tuple[Pos, ...]]] = [(0, beg_pos, ())]
        # min_dist = {}
        seen = set()
        paths = []

        while queue:
            dist, pos, path = hq.heappop(queue)
            if pos in fins_pos:
                hq.heappush(paths, (dist, path))
                continue
            if pos in seen or pos in occupied:
                continue
            seen.add(pos)

            for nxt in pos.near:
                if nxt in self.tiles and (
                    nxt not in occupied or nxt in fins_pos
                ):
                    hq.heappush(queue, (dist + 1, nxt, path + (nxt,)))

        if paths:
            paths.sort(key=lambda t: (t[0], t[1][-1], t[1][0]))
            return paths[0][1][0]
        else:
            return None

    def round(self, loss_allowed=True):
        self.units.sort(key=lambda u: u.pos)

        for unit in self.units:
            if unit.dead:
                continue

            targets = [
                u for u in self.units if (u.elf != unit.elf) and not u.dead
            ]
            if not targets:
                return False

            near = [u for u in targets if u.pos in unit.pos.near]

            if not near:
                nxt_pos = self.move(unit, targets)
                if nxt_pos is None:
                    continue
                unit.pos = nxt_pos

            near = [u for u in targets if u.pos in unit.pos.near]

            if near:
                near.sort(key=lambda u: (u.hp, *u.pos))
                near[0].hp -= unit.power
                if near[0].hp <= 0:
                    if near[0].elf and not loss_allowed:
                        raise ElfRIP()
                    near[0].dead = True

        return True

    def game(self, loss_allowed=True):
        i = 0
        while self.round(loss_allowed=loss_allowed):
            i += 1
        fin_hp = sum(u.hp for u in self.units if not u.dead)
        return i * fin_hp


if __name__ == "__main__":
    with open("_inputs/2018/day-15/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip("\n").split("\n")

    t0 = time.time()
    result = Cave(lines).game(True)
    print(f"Part 1: {result}")
    print(f"    took {time.time() - t0:.2f} secs")

    t0 = time.time()
    power = 4
    while True:
        try:
            result = Cave(lines, power).game(False)
        except ElfRIP:
            power += 1
            continue
        else:
            print(f"Part 2: {result} with power {power}")
            print(f"    took {time.time() - t0:.2f} secs")
            break
