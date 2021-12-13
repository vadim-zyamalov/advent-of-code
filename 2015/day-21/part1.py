import math

player = {'hp': 100}

weapons = {}
armor = {}
rings = {}


def items_permute(weapons, armor, rings):
    for w in weapons:
        for a in armor:
                for r1 in rings:
                    for r2 in [k for k in rings if k != r1]:
                        yield (w, a, r1, r2)


def fight(player, boss):
    while True:
        boss['hp'] -= max(1, player['damage'] - boss['armor'])
        if boss['hp'] <= 0:
            return True
        player['hp'] -= max(1, boss['damage'] - player['armor'])
        if player['hp'] <= 0:
            return False


with open("items.txt", "r") as f:
    while True:
        line = f.readline()
        if line == '':
            break
        if line.startswith("Weapons"):
            while True:
                line = f.readline().strip()
                if line == '':
                    break
                tmp = line.split()
                weapons[tmp[0]] = {'cost': int(tmp[-3]),
                                   'damage': int(tmp[-2]),
                                   'armor': int(tmp[-1])}
        if line.startswith("Armor"):
            while True:
                line = f.readline().strip()
                if line == '':
                    break
                tmp = line.split()
                armor[tmp[0]] = {'cost': int(tmp[-3]),
                                 'damage': int(tmp[-2]),
                                 'armor': int(tmp[-1])}
            armor['no'] = {'cost': 0,
                           'damage': 0,
                           'armor': 0}
        if line.startswith("Rings"):
            while True:
                line = f.readline().strip()
                if line == '':
                    break
                tmp = line.split()
                rings[' '.join(tmp[0:2])] = {'cost': int(tmp[-3]),
                                             'damage': int(tmp[-2]),
                                             'armor': int(tmp[-1])}
                rings['no 1'] = {'cost': 0,
                                 'damage': 0,
                                 'armor': 0}
                rings['no 2'] = {'cost': 0,
                                 'damage': 0,
                                 'armor': 0}


boss = {}
with open("input.txt") as f:
    for line in f:
        _, val = line.strip().split(":")
        if line.startswith("Hit Points"):
            boss['hp'] = int(val.strip())
        if line.startswith("Damage"):
            boss['damage'] = int(val.strip())
        if line.startswith("Armor"):
            boss['armor'] = int(val.strip())

costs = []
for p in items_permute(weapons,
                       armor,
                       rings):
    player['damage'] = weapons[p[0]]['damage'] + armor[p[1]]['damage'] + rings[p[2]]['damage'] + rings[p[3]]['damage']
    player['armor']  = weapons[p[0]]['armor'] + armor[p[1]]['armor'] + rings[p[2]]['armor'] + rings[p[3]]['armor']

    if fight(player.copy(), boss.copy()):
        tmp = 0
        tmp += weapons[p[0]]['cost']
        tmp += armor[p[1]]['cost']
        tmp += rings[p[2]]['cost']
        tmp += rings[p[3]]['cost']
        costs.append(tmp)
print("Part 1: {}".format(min(costs)))

costs = []
for p in items_permute(weapons,
                       armor,
                       rings):
    player['damage'] = weapons[p[0]]['damage'] + armor[p[1]]['damage'] + rings[p[2]]['damage'] + rings[p[3]]['damage']
    player['armor']  = weapons[p[0]]['armor'] + armor[p[1]]['armor'] + rings[p[2]]['armor'] + rings[p[3]]['armor']

    if not fight(player.copy(), boss.copy()):
        tmp = 0
        tmp += weapons[p[0]]['cost']
        tmp += armor[p[1]]['cost']
        tmp += rings[p[2]]['cost']
        tmp += rings[p[3]]['cost']
        costs.append(tmp)
print("Part 2: {}".format(max(costs)))
