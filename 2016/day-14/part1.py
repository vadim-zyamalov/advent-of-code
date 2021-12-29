from functools import cache
import hashlib


def check_hash3(data):
    for idx in range(len(data) - 2):
        if (data[idx] == data[idx + 1]) and \
                (data[idx] == data[idx + 2]):
            return data[idx]
    return None


def check_hash5(data, val):
    test = val * 5
    return test in data


@cache
def get_hash(i):
    return hashlib.md5(f"{SALT}{i}".encode()).hexdigest()


@cache
def get_hash_stretched(i):
    tmp = hashlib.md5(f"{SALT}{i}".encode()).hexdigest()
    for _ in range(2016):
        tmp = hashlib.md5(tmp.encode()).hexdigest()
    return tmp


SALT = "ahsbgdzn"
# SALT = "abc"
index = 0
key_num = 0

while key_num < 64:
    tmp_val = check_hash3(get_hash(index))
    if tmp_val is not None:
        for j in range(1, 1001):
            if check_hash5(get_hash(index + j), tmp_val):
                key_num += 1
                break
    index += 1

print(f"Part 1: {index-1}")


index = 0
key_num = 0

while key_num < 64:
    tmp_val = check_hash3(get_hash_stretched(index))
    if tmp_val is not None:
        for j in range(1, 1001):
            if check_hash5(get_hash_stretched(index + j), tmp_val):
                key_num += 1
                break
    index += 1

print(f"Part 2: {index-1}")
