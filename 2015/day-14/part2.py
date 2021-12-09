deer   = []
speed  = []
flight = []
rest   = []
score  = []

with open("input.txt", "r") as f:
    for line in f:
        string = line.strip().strip('.').split()
        deer.append(string[0])
        speed.append(int(string[3]))
        flight.append(int(string[6]))
        rest.append(int(string[-2]))
        score.append(0)
dist = [0 for _ in range(len(deer))]

period = 2503
for t in range(1, period + 1):
    winner = 0
    for i in range(len(deer)):
        total_flying = flight[i] * (t // (flight[i] + rest[i])) + \
            min(t % (flight[i] + rest[i]), flight[i])
        dist[i] = total_flying * speed[i]
    winner = max(dist)
    for i in range(len(deer)):
        if dist[i] == winner:
            score[i] += 1

winner = max(score)

print("Part 2: {}".format(winner))
