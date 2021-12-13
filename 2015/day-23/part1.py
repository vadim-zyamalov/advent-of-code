def execute(program, init = {'a': 0, 'b': 0}):
    registers = init.copy()

    i = 0
    while i < len(program):
        current = program[i]
        if current['c'] not in allowed:
            break
        if current['c'] == 'hlf':
            registers[current['r']] //= 2
            i += 1
        elif current['c'] == 'tpl':
            registers[current['r']] *= 3
            i += 1
        elif current['c'] == 'inc':
            registers[current['r']] += 1
            i += 1
        elif current['c'] == 'jmp':
            i += current['o']
        elif current['c'] == 'jie':
            if registers[current['r']] % 2 == 0:
                i += current['o']
            else:
                i += 1
        elif current['c'] == 'jio':
            if registers[current['r']] == 1:
                i += current['o']
            else:
                i += 1
    return registers


program = []
allowed = ['hlf',
           'tpl',
           'inc',
           'jmp',
           'jie',
           'jio']

with open("input.txt", "r") as f:
    for line in f:
        if line.strip() == '':
            continue
        tmp = line.strip().split()
        if len(tmp) == 2:
            if tmp[0] == 'jmp':
                program.append({'c': 'jmp',
                                'r': None,
                                'o': int(tmp[1])})
            else:
                program.append({'c': tmp[0],
                                'r': tmp[1],
                                'o': None})
        else:
            program.append({'c': tmp[0],
                            'r': tmp[1].replace(',', ''),
                            'o': int(tmp[2])})


# Part 1
print("Part 1: {}".format(execute(program)))

# Part 2
print("Part 2: {}".format(execute(program,
                                  {'a': 1, 'b': 0})))
