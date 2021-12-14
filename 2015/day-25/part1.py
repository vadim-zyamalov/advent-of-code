row = 2947
col = 3029

fcol = col + (row - 1)
num = sum(i for i in range(1, fcol + 1)) - (row - 1)

code = 20151125

for _ in range(2, num + 1):
    code = (code * 252533) % 33554393

print("Part 1: {}".format(code))
