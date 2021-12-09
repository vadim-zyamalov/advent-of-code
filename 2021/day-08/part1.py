segments = {1: 2,
            4: 4,
            7: 3,
            8: 7}
lengths = list(segments.values())

ans = 0
with open("input.txt", "r") as f:
    for line in f:
        patterns, _, output = line.strip().partition(' | ')
        output_d = [d for d in output.split()]
        for d in output_d:
            if len(d) in lengths:
                ans += 1
print("Part 1: {}".format(ans))
