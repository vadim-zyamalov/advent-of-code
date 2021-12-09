def filter(llist, pos, most):
    count = sum([int(i[pos]) for i in llist])
    total = len(llist)
    if most:
        if count < total / 2:
            return [i for i in llist if i[pos] == '0']
        else:
            return [i for i in llist if i[pos] == '1']
    else:
        if count >= total / 2:
            return [i for i in llist if i[pos] == '0']
        else:
            return [i for i in llist if i[pos] == '1']

diag = []
with open("input.txt", "r") as f:
    for line in f:
        diag.append(line.strip())

oxy_diag = diag.copy()
for i in range(len(oxy_diag[0])):
    if len(oxy_diag) == 1:
        break
    oxy_diag = filter(oxy_diag, i, True)

oxy = int('0b' + oxy_diag[0], 2)

co2_diag = diag.copy()
for i in range(len(co2_diag[0])):
    if len(co2_diag) == 1:
        break
    co2_diag = filter(co2_diag, i, False)

co2 = int('0b' + co2_diag[0], 2)

print("Part 1: {}".format(oxy * co2))
