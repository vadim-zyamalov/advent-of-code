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

            if len(left) == 1:
                signal[right] = uint16(left[0]) if \
                    left[0].isnumeric() else None
                matrix[right] = {'arg': [left[0]
                                         if not left[0].isnumeric() else None],
                                 'sig': [uint16(left[0])
                                         if left[0].isnumeric() else None],
                                 'fun': ''}
            elif len(left) == 2:
                signal[right] = None
                matrix[right] = {'arg': [left[1]
                                         if not left[1].isnumeric() else None],
                                 'sig': [uint16(left[1])
                                         if left[1].isnumeric() else None],
                                 'fun': left[0]}
            elif len(left) == 3:
                signal[right] = None
                matrix[right] = {'arg': [left[0]
                                         if not left[0].isnumeric() else None,
                                         left[2]
                                         if not left[2].isnumeric() else None],
                                 'sig': [uint16(left[0])
                                         if left[0].isnumeric() else None,
                                         uint16(left[2])
                                         if left[2].isnumeric() else None],
                                 'fun': left[1]}

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
            if signal[k] is None and all(v is not None for v in entry['sig']):
                if entry['fun'] == 'NOT':
                    signal[k] = ~ entry['sig'][0]
                elif entry['fun'] == 'AND':
                    signal[k] = entry['sig'][0] & entry['sig'][1]
                elif entry['fun'] == 'OR':
                    signal[k] = entry['sig'][0] | entry['sig'][1]
                elif entry['fun'] == 'LSHIFT':
                    signal[k] = entry['sig'][0] << entry['sig'][1]
                elif entry['fun'] == 'RSHIFT':
                    signal[k] = entry['sig'][0] >> entry['sig'][1]
                else:
                    signal[k] = entry['sig'][0]
                matrix = update_matrix(k, signal[k])

    print(f"Part {part}: {signal['a']}")
