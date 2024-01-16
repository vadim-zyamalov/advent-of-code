import re
from collections import defaultdict


class Group:
    def __init__(self, line, team, no):
        self.id = f"{team}_{no}"
        self.immune = team == "immune"

        res = re.findall(r"(\d*) units", line)
        self.N = int(res[0])

        res = re.findall(r"(\d*) hit", line)
        self.hp = int(res[0])

        res = re.findall(r"(\d*) ([^\s]*) damage", line)
        self.dmg, self.attack = res[0]
        self.dmg = int(self.dmg)

        res = re.findall(r"initiative (\d*)", line)
        self.initiative = int(res[0])

        self.weak = []
        self.resist = []

        res = re.findall(r"\((.*)\)", line)
        if res:
            for chunk in res[0].replace(",", "").split(";"):
                chunk = chunk.strip().split()
                if chunk[0] == "weak":
                    self.weak.extend(chunk[2:])
                else:
                    self.resist.extend(chunk[2:])

    def __repr__(self):
        result = (
            f"{self.id}, N: {self.N}, hp: {self.hp}, {self.attack}:{self.dmg}"
        )
        if self.weak:
            result += f", weak: {', '.join(self.weak)}"
        if self.resist:
            result += f", resist: {', '.join(self.resist)}"
        return f"[{result}]"

    def power(self, boost=0):
        return self.N * (self.dmg + (boost if self.immune else 0))

    def suffer(self, damage):
        killed = damage // self.hp
        self.N -= killed


class Game:
    def __init__(self, lines):
        self.groups = []

        current_team = "immune"
        no = 0

        for line in lines:
            if line == "":
                continue
            if line.startswith("Immune"):
                current_team = "immune"
                no = 0
            elif line.startswith("Infection"):
                current_team = "infection"
                no = 0
            else:
                self.groups.append(Group(line, current_team, no))
                no += 1

    def ph_selection(self, boost=0):
        targets = {}

        self.groups.sort(
            key=lambda g: (g.power(boost), g.initiative), reverse=True
        )

        for g in self.groups:
            max_dmg = 0
            tgt = ""
            for eg in self.groups:
                if eg.immune == g.immune:
                    continue
                if eg.id in targets.values():
                    continue
                if g.attack in eg.resist:
                    continue
                pos_dmg = (g.power(boost)) * (2 if g.attack in eg.weak else 1)
                if pos_dmg > max_dmg:
                    max_dmg = pos_dmg
                    tgt = eg.id
            if max_dmg > 0:
                targets[g.id] = tgt
        return targets

    def ph_attack(self, targets, boost=0):
        self.groups.sort(key=lambda g: g.initiative, reverse=True)

        for g in self.groups:
            if g.N <= 0:
                continue
            if g.id not in targets:
                continue

            eg = [el for el in self.groups if el.id == targets[g.id]][0]
            dmg = g.power(boost) * (2 if g.attack in eg.weak else 1)
            eg.suffer(dmg)

    def move(self, boost=0):
        if sum(g.immune for g in self.groups) and sum(
            not g.immune for g in self.groups
        ):
            targets = self.ph_selection(boost)
            if targets == {}:
                return False
            self.ph_attack(targets, boost)
            self.groups = [g for g in self.groups if g.N > 0]
            return True
        return False


if __name__ == "__main__":
    with open("_inputs/2018/day-24/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip().split("\n")

    game = Game(lines)

    while game.move():
        pass

    result = sum(g.N for g in game.groups)
    print(f"Part 1: {result}")

    boost = 0
    delta = 100

    while delta > 0:
        while True:
            game = Game(lines)

            while game.move(boost):
                pass

            result = sum(g.N for g in game.groups if g.immune)
            enemies = sum(g.N for g in game.groups if not g.immune)
            if (result > 0) and (enemies == 0):
                if delta == 1:
                    print(f"Part 2: {result} with boost=={boost}")
                break
            boost += delta
        boost -= delta
        delta //= 10
