from collections import deque
import numpy as np


def next_pos(x, y, garden):
    Nx, Ny = len(garden), len(garden[0])
    result = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if garden[(x + dx) % Nx][(y + dy) % Ny] != "#":
            result.append((x + dx, y + dy))
    return result


def get_start(garden):
    for i, row in enumerate(garden):
        for j, el in enumerate(row):
            if el == "S":
                return (i, j)
    assert False


def part1(max_step, garden):
    visited = set()
    possible = set()
    resid = max_step % 2
    bx, by = get_start(garden)
    queue = deque()
    queue.append((0, bx, by))

    while queue:
        step, x, y = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))
        if (step % 2 == resid) and ((x, y) not in possible):
            possible.add((x, y))

        if step < max_step:
            for nx, ny in next_pos(x, y, garden):
                queue.append((step + 1, nx, ny))

    return len(possible)


def part2(steps, garden):
    x0 = steps % len(garden)
    x = steps // len(garden)

    A = np.array([[0, 0, 1], [1, 1, 1], [4, 2, 1]], dtype=np.int64)
    b = np.array(
        [
            [
                part1(x0, garden),
                part1(x0 + len(garden), garden),
                part1(x0 + 2 * len(garden), garden),
            ]
        ],
        dtype=np.int64,
    ).T

    result = np.array([x**2, x, 1]) @ (np.linalg.inv(A) @ b).astype(np.int64)

    return int(result)


if __name__ == "__main__":
    with open("_inputs/2023/day-21/input.txt") as f:
        garden = f.read().strip().split("\n")

        beg = get_start(garden)

        res1 = part1(64, garden)
        print(f"Part 1: {res1}")

        res2 = part2(26501365, garden)
        print(f"Part 2: {res2}")
