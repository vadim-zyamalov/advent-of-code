deers = {}

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        string = line.strip().strip('.').split()
        deers[string[0]] = {'speed': int(string[3]),
                            'flying': int(string[6]),
                            'resting': int(string[-2])}

period = 2503
winner = 0
for _, deer in deers.items():
    total_flying = deer['flying'] * \
        (period // (deer['flying'] + deer['resting'])) + \
        min(period % (deer['flying'] + deer['resting']),
            deer['flying'])
    deer['dist'] = total_flying * deer['speed']
    winner = deer['dist'] if deer['dist'] > winner else winner

print(f"Part 1: {winner}")
