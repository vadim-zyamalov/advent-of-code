import sys
import time
from collections import deque
from typing import Deque

sys.path.append(".\\")

from utils.intcode import Intcode, State

PROHIBITED = [
    "escape pod",
    "infinite loop",
    "molten lava",
    "photons",
    "giant electromagnet",
]

FINISH = "Security Checkpoint"
CHECKER = "Pressure-Sensitive Floor"


def to_string(output):
    return str("".join(map(chr, output)))


def parse(output):
    output = output.strip()
    output = output.split("\n\n")

    _wght = 0
    _doors = []
    _items = []
    _room = ""

    for part in output:
        part = part.strip()
        part = part.split("\n")

        if part[0].startswith("="):
            _room = part[0].strip("= ")
        elif part[0].startswith("Doors"):
            _doors = [el.strip("- ") for el in part[1:]]
        elif part[0].startswith("Items"):
            _items = [el.strip("- ") for el in part[1:]]
        elif part[0].startswith("A loud"):
            if "lighter" in part[0]:
                _wght = -1
            elif "heavier" in part[0]:
                _wght = 1

    return _room, _doors, _items, _wght


def collect(computer, initmsg) -> tuple[str, frozenset, State]:
    seen = set()
    queue: Deque[tuple[str, frozenset, str, State]] = deque(
        [("Hull Breach", frozenset(), initmsg, computer.save())]
    )

    _msg = ""
    _inv = frozenset()
    _state = computer.save()

    while queue:
        room, inv, msg, state = queue.popleft()

        if room == FINISH:
            if len(inv) <= len(_inv):
                continue
            _msg = msg
            _inv = inv
            _state = state

        if (room, inv) in seen:
            continue
        seen.add((room, inv))

        _, doors, items, _ = parse(msg)

        if items and (item := items[0]) not in PROHIBITED:
            computer.load(state)
            computer.resume(inputs=f"take {item}")
            state = computer.save()
            inv |= {item}

        for door in doors:
            computer.load(state)
            output = computer.resume(inputs=f"{door}")
            nxt, _, _, _ = parse(output.ascii)
            queue.append((nxt, inv, output.ascii, computer.save()))
    return _msg, _inv, _state


def weight(computer, inv, door):
    for item in inv:
        computer.resume(inputs=f"drop {item}")

    queue = deque()
    state = computer.save()

    # Добавляем в очередь первый возможный из всех наборов
    for item in inv:
        computer.load(state)
        computer.resume(inputs=f"take {item}")
        output = computer.resume(inputs=f"{door}")
        _, _, _, _wght = parse(output.ascii)
        if _wght == 0:
            print(f"Set found: [{item}]")
            print(to_string(output))
            return
        elif _wght > 0:
            queue.append((frozenset({item}), computer.save()))

    # Начинаем формировать наборы, присоединяя по одному объекту
    # к уже имеющимся
    seen = set()
    while queue:
        items, state = queue.popleft()
        for item in inv:
            if item in items:
                continue
            _items = items | {item}

            if _items in seen:
                continue
            seen.add(_items)

            computer.load(state)
            computer.resume(inputs=f"take {item}")
            output = computer.resume(inputs=f"{door}")
            _, _, _, _wght = parse(output.ascii)

            if _wght == 0:
                print(f"Set found: [{', '.join(_items)}]")
                print(output.ascii)
                return
            elif _wght > 0:
                queue.append((_items, computer.save()))


if __name__ == "__main__":
    with open("_inputs/2019/day-25/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split(",")))

    computer = Intcode(numbers, ascii=True)
    output = computer.start(inputs=[])

    _msg, _inv, _state = collect(computer, output.ascii)

    _, doors, _, _ = parse(_msg)

    door = "west"

    if len(doors) == 1:
        [door] = doors
    else:
        for d in doors:
            computer.load(_state)
            output = computer.resume(inputs=f"{d}")
            _room, _, _, _ = parse(output.ascii)
            if _room == CHECKER:
                door = d
                break

    computer.load(_state)
    weight(computer, _inv, door)
