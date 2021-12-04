import json


def dive(data):
    ans = 0
    if isinstance(data, dict):
        for i in data:
            if isinstance(data[i], str) and (data[i] == 'red'):
                return 0
        for i in data:
            tmp = dive(data[i])
            if tmp:
                ans += tmp
        return ans
    elif isinstance(data, list):
        for i in data:
            tmp = dive(i)
            if tmp:
                ans += tmp
        return ans
    elif isinstance(data, int):
        return data
    else:
        return 0


with open("input.txt", "r") as f:
    data = json.load(f)

print(dive(data))
