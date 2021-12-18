segments = {1: 2,
            4: 4,
            7: 3,
            8: 7}
lengths = list(segments.values())

answer = 0
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        patterns, _, output = line.strip().partition(' | ')
        output_d = list(output.split())
        for d in output_d:
            if len(d) in lengths:
                answer += 1
print(f"Part 1: {answer}")
