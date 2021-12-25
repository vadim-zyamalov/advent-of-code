class Node:
    def __init__(self, value=None, left=None, right=None, parent=None) -> None:
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


def dump(root):
    if root.value is not None:
        print(root.value, sep="", end="")
    else:
        print("{", sep="", end="")
        dump(root.left)
        print(",", sep="", end="")
        dump(root.right)
        print("}", sep="", end="")
    if root.parent is None:
        print()


def parse(number: str) -> Node:
    if number[0] != '[':
        return Node(int(number))
    result = Node()
    tmp = ''
    count = 0
    for letter in number[1:-1]:
        if letter == '[':
            tmp += letter
            count += 1
        elif letter == ']':
            tmp += letter
            count -= 1
        elif (letter == ',') and \
             (count == 0):
            result.left = parse(tmp)
            result.left.parent = result
            tmp = ''
        else:
            tmp += letter
    if tmp != '':
        result.right = parse(tmp)
        result.right.parent = result
    return result


def inc_left(val, node: Node) -> None:
    prev = node
    cur = node.parent
    while cur is not None:
        if cur.left == prev:
            prev = cur
            cur = cur.parent
        else:
            break
    if cur is not None:
        cur = cur.left
        while cur.value is None:
            cur = cur.right
        cur.value += val


def inc_right(val, node: Node) -> None:
    prev = node
    cur = node.parent
    while cur is not None:
        if cur.right == prev:
            prev = cur
            cur = cur.parent
        else:
            break
    if cur is not None:
        cur = cur.right
        while cur.value is None:
            cur = cur.left
        cur.value += val


def explode(root: Node, depth=1):
    if root.left is not None and \
            root.right is not None and \
            root.left.value is not None and \
            root.right.value is not None:
        if depth > 4:
            a = root.left.value
            b = root.right.value
            root.value = 0
            root.left = None
            root.right = None
            inc_left(a, root)
            inc_right(b, root)
            return True
        else:
            return False
    result = False
    if root.left is not None:
        result = explode(root.left, depth + 1)
    if result is False:
        if root.right is not None:
            result = explode(root.right, depth + 1)
    return result


def split(root: Node):
    if root.value is not None:
        if root.value > 9:
            a, b = root.value // 2, (root.value + 1) // 2
            root.value = None
            root.left = Node(a, None, None, root)
            root.right = Node(b, None, None, root)
            return True
        else:
            return False
    else:
        result = split(root.left)
        if result is False:
            result = split(root.right)
        return result


def reduce(root: Node):
    while True:
        if explode(root, 1):
            continue
        if split(root):
            continue
        break


def magnitude(root: Node):
    if root.value is not None:
        return root.value
    return 3 * magnitude(root.left) + 2 * magnitude(root.right)


def num_add(n1: Node, n2: Node):
    result = Node()
    result.left = n1
    result.left.parent = result
    result.right = n2
    result.right.parent = result
    return result


numbers = []
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        numbers.append(line.strip())

# parsed = parse(numbers[0])
# print(numbers[0])
# dump(parsed)
# reduce(parsed)
# dump(parsed)

answer = parse(numbers[0])
for number in numbers[1:]:
    answer = num_add(answer, parse(number))
    reduce(answer)
answer = magnitude(answer)
print(f"Part 1: {answer}")

answer = []
for i, number1 in enumerate(numbers):
    for j, number2 in enumerate(numbers):
        if i == j:
            continue
        tmp = num_add(parse(number1), parse(number2))
        reduce(tmp)
        answer.append(magnitude(tmp))

print(f"Part 2: {max(answer)}")

