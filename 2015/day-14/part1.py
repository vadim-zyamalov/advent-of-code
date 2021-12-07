deers = {}

with open("input.txt", "r") as f:
    for line in f:
        string = line.strip().strip('.').split()
        deers[string[0]] = {'speed': int(string[3]),
                            'flying': int(string[6]),
                            'resting': int(string[-2])}

period = 2503
winner = 0
for k in deers:
    total_flying = deers[k]['flying'] * (period // (deers[k]['flying'] + deers[k]['resting'])) + \
         min(period % (deers[k]['flying'] + deers[k]['resting']), deers[k]['flying'])
    deers[k]['dist'] = total_flying * deers[k]['speed']
    winner = deers[k]['dist'] if deers[k]['dist'] > winner else winner

print(winner)
