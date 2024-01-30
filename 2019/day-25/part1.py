import sys
import time
from collections import deque
from typing import Deque

sys.path.append(".\\")

from utils.intcode import Intcode

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
    if not isinstance(output, str):
        _output = to_string(output)
    else:
        _output = output
    _output = _output.strip()
    _output = _output.split("\n\n")

    _wght = 0
    _doors = []
    _items = []
    _room = ""

    for part in _output:
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


def collect(computer, initmsg):
    seen = set()
    queue: Deque[tuple[str, frozenset, str, tuple]] = deque(
        [("Hull Breach", frozenset(), initmsg, computer.save())]
    )

    _msg = ""
    _inv = frozenset()
    _state = ()

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
            computer.load(*state)
            computer.process(inputs=f"take {item}", ascii=True, resume=True)
            state = computer.save()
            inv |= {item}

        for door in doors:
            computer.load(*state)
            output, _ = computer.process(
                inputs=f"{door}", ascii=True, resume=True
            )
            output = to_string(output)
            nxt, _, _, _ = parse(output)
            queue.append((nxt, inv, output, computer.save()))
    return _msg, _inv, _state


def weight(computer, inv, door):
    for item in inv:
        computer.process(inputs=f"drop {item}", ascii=True, resume=True)

    queue = deque()
    state = computer.save()

    # Добавляем в очередь первый возможный из всех наборов
    for item in inv:
        computer.load(*state)
        computer.process(inputs=f"take {item}", ascii=True, resume=True)
        output, _ = computer.process(inputs=f"{door}", ascii=True, resume=True)
        _, _, _, _wght = parse(output)
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

            computer.load(*state)
            computer.process(inputs=f"take {item}", ascii=True, resume=True)
            output, _ = computer.process(
                inputs=f"{door}", ascii=True, resume=True
            )
            _, _, _, _wght = parse(output)

            if _wght == 0:
                print(f"Set found: [{', '.join(_items)}]")
                print(to_string(output))
                return
            elif _wght > 0:
                queue.append((_items, computer.save()))


if __name__ == "__main__":
    with open("_inputs/2019/day-25/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split(",")))

    computer = Intcode(numbers)
    output, _ = computer.process(inputs=[])
    output = to_string(output)

    _msg, _inv, _state = collect(computer, output)

    _, doors, _, _ = parse(_msg)

    door = "west"

    if len(doors) == 1:
        [door] = doors
    else:
        for d in doors:
            computer.load(*_state)
            output, _ = computer.process(inputs=f"{d}", ascii=True, resume=True)
            _room, _, _, _ = parse(output)
            if _room == CHECKER:
                door = d
                break

    computer.load(*_state)
    weight(computer, _inv, door)
