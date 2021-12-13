def dump(results):
    i = 0
    for r in results:
        i += 1
        print("{} : {}".format(i, r))
    print()


def effect(player, boss, timer, spells):
    for s in timer:
        if timer[s] > 0:
            if s == 'Poison':
                boss['hp'] -= spells[s]['damage']
            if s == 'Recharge':
                player['mana'] += spells[s]['mana']
            timer[s] -= 1
            if (timer[s] == 0) and (s == 'Shield'):
                player['armor'] = 0


def player_turn(player, boss, timer, spells):
    player['hp'] -= difficulty
    if player['hp'] <= 0:
        return [(False, 0)]
    effect(player, boss, timer, spells)
    if boss['hp'] <= 0:
        return [(True, 0)]
    result = []
    for s in spells:
        if (player['mana'] >= spells[s]['cost']) and \
           (timer[s] == 0):
            loop_player = player.copy()
            loop_boss = boss.copy()
            loop_timer = timer.copy()
            loop_player['mana'] -= spells[s]['cost']
            if s in ['Magic Missile', 'Drain']:
                loop_boss['hp'] -= spells[s]['damage']
                loop_player['hp'] += spells[s]['hp']
            else:
                if s == 'Shield':
                    loop_player['armor'] = spells[s]['armor']
                loop_timer[s] = spells[s]['duration']
            tmp_result = boss_turn(loop_player.copy(), loop_boss.copy(), loop_timer.copy(), spells)
            if tmp_result:
                for tmp in tmp_result:
                    result.append((tmp[0], spells[s]['cost'] + tmp[1]))
    if result == []:
        return [(False, 0)]
    return result


def boss_turn(player, boss, timer, spells):
    effect(player, boss, timer, spells)
    if player['hp'] <= 0:
        return [(False, 0)]
    if boss['hp'] <= 0:
        return [(True, 0)]
    player['hp'] -= max(1, boss['damage'] - player['armor'])
    return player_turn(player.copy(), boss.copy(), timer.copy(), spells)


spells = {}
with open("spells.txt", "r") as f:
    for line in f:
        if line.startswith('Name'):
            continue
        tmp = line.strip().split()
        res = {'cost': int(tmp[-6]),
               'damage': int(tmp[-5]),
               'armor': int(tmp[-4]),
               'duration': int(tmp[-3]),
               'hp': int(tmp[-2]),
               'mana': int(tmp[-1])}
        spells[' '.join(tmp[:-6])] = res

timer = {}
for k in spells:
    timer[k] = 0

player = {'hp': 50,
          'mana': 500,
          'armor': 0}

boss = {}
with open("input.txt", "r") as f:
    line = f.readline()
    _, val = line.strip().split(':')
    boss['hp'] = int(val.strip())
    line = f.readline()
    _, val = line.strip().split(':')
    boss['damage'] = int(val.strip())

# Part 1
difficulty = 0
result = player_turn(player.copy(),
                     boss.copy(),
                     timer.copy(),
                     spells)
min_mana = min(r[1] for r in result if r[0] == True)
print("Part 1: {}".format(min_mana))

# Part 2
difficulty = 1
result = player_turn(player.copy(),
                     boss.copy(),
                     timer.copy(),
                     spells)
min_mana = min(r[1] for r in result if r[0] == True)
print("Part 2: {}".format(min_mana))
