grid = []

moves = [(-1, 0),
		 (0, -1)]


def dump(grid):
	for row in grid:
		for digit in row:
			print(digit, end=" ")
		print()
	print()


def deep_copy(grid):
	return [[el for el in raw] for raw in grid]


def process(grid):
	dimi, dimj = len(grid), len(grid[0])
	inner_grid = deep_copy(grid)
	for step in range(dimi):
		for s in range(step, dimi):
			tmpr = []
			tmpc = []
			for di, dj in moves:
				if (0 <= step + di < dimi) and \
				   (0 <= s + dj < dimj):
					tmpr.append(inner_grid[step + di][s + dj])
				if (0 <= s + di < dimi) and \
				   (0 <= step + dj < dimj):
					tmpc.append(inner_grid[s + di][step + dj]) 
			if tmpr:
				inner_grid[step][s] += min(tmpr)
			if tmpc and (step != s):
				inner_grid[s][step] += min(tmpc)
	return inner_grid


with open("input.txt", "r") as f:
	for line in f:
		if line.strip() == "":
			continue
		grid.append([int(digit) for digit in line.strip()])

# dump(grid)

result = process(grid)
print(result[len(result) - 1][len(result) - 1] - result[0][0])
# dump(result)
