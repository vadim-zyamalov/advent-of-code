from numpy import uint16

signal = {}
matrix = {}


def update_matrix(code, val, matrix=matrix):
    for k in matrix:
        if code in matrix[k]['arg']:
            index = matrix[k]['arg'].index(code)
            matrix[k]['sig'][index] = val
    return matrix


for part in [1, 2]:
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            left, right = line.strip().split('->')

            right = right.strip()
            left = left.strip().split()

            match left:
                case arg_0, :
                    signal[right] = uint16(arg_0) if \
                        arg_0.isnumeric() else None
                    matrix[right] = {'arg': [arg_0
                                             if not arg_0.isnumeric() else None],
                                     'sig': [uint16(arg_0)
                                             if arg_0.isnumeric() else None],
                                     'fun': ''}
                case arg_0, arg_1:
                    signal[right] = None
                    matrix[right] = {'arg': [arg_1
                                             if not arg_1.isnumeric() else None],
                                     'sig': [uint16(arg_1)
                                             if arg_1.isnumeric() else None],
                                     'fun': arg_0}
                case arg_0, arg_1, arg_2:
                    signal[right] = None
                    matrix[right] = {'arg': [arg_0
                                             if not arg_0.isnumeric() else None,
                                             arg_2
                                             if not arg_2.isnumeric() else None],
                                     'sig': [uint16(arg_0)
                                             if arg_0.isnumeric() else None,
                                             uint16(arg_2)
                                             if arg_2.isnumeric() else None],
                                     'fun': arg_1}

    if part == 2:
        signal['b'] = uint16(956)
        matrix['b'] = {'arg': [''],
                       'sig': [signal['b']],
                       'fun': ''}

    for k in signal:
        if signal[k] is not None:
            matrix = update_matrix(k, signal[k])

    while signal['a'] is None:
        for k in matrix:
            entry = matrix[k]
            if signal[k] is not None:
                continue
            if not all(v is not None for v in entry['sig']):
                continue
            match entry['fun']:
                case 'NOT':
                    signal[k] = ~ entry['sig'][0]
                case 'AND':
                    signal[k] = entry['sig'][0] & entry['sig'][1]
                case 'OR':
                    signal[k] = entry['sig'][0] | entry['sig'][1]
                case 'LSHIFT':
                    signal[k] = entry['sig'][0] << entry['sig'][1]
                case 'RSHIFT':
                    signal[k] = entry['sig'][0] >> entry['sig'][1]
                case _:
                    signal[k] = entry['sig'][0]
            matrix = update_matrix(k, signal[k])

    print(f"Part {part}: {signal['a']}")
