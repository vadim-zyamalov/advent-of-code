import time


class Node:
    def __init__(self,
                 value: int = None,
                 left: "Node" = None,
                 right: "Node" = None,
                 parent: "Node" = None) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def dump(root: Node) -> None:
    assert root is not None
    if root.value is not None:
        print(root.value, sep="", end="")
    else:
        assert root.left is not None
        assert root.right is not None
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
    assert node is not None
    prev = node
    cur = node.parent
    while cur is not None:
        if cur.left == prev:
            prev = cur
            cur = cur.parent
        else:
            break
    if cur is not None:
        assert cur.left is not None
        cur = cur.left
        while cur.value is None:
            assert cur.right is not None
            cur = cur.right
        cur.value += val


def inc_right(val, node: Node) -> None:
    assert node is not None
    prev = node
    cur = node.parent
    while cur is not None:
        if cur.right == prev:
            prev = cur
            cur = cur.parent
        else:
            break
    if cur is not None:
        assert cur.right is not None
        cur = cur.right
        while cur.value is None:
            assert cur.left is not None
            cur = cur.left
        cur.value += val


def explode(root: Node, depth=1) -> bool:
    assert root is not None
    # Check whether we found a pair of literal numbers
    if root.left is not None and \
            root.right is not None and \
            root.left.value is not None and \
            root.right.value is not None:
        # Check whether we are deeper than the 4-th level
        if depth > 4:
            a = root.left.value
            b = root.right.value
            # Turn the pair into the literal number
            root.value = 0
            root.left = None
            root.right = None
            # Increase the first literal on the left
            inc_left(a, root)
            # Increase the first literal on the right
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


def split(root: Node) -> bool:
    assert root is not None
    if root.value is not None:
        if root.value > 9:
            a, b = root.value // 2, (root.value + 1) // 2
            # Turn the literal number to th pair of literal numbers
            root.value = None
            root.left = Node(a, None, None, root)
            root.right = Node(b, None, None, root)
            return True
        else:
            return False
    else:
        assert root.left is not None
        result = split(root.left)
        if result is False:
            assert root.right is not None
            result = split(root.right)
        return result


def reduce(root: Node) -> None:
    assert root is not None
    while True:
        if explode(root, 1):
            continue
        if split(root):
            continue
        break


def magnitude(root: Node) -> int:
    assert root is not None
    if root.value is not None:
        return root.value
    assert root.left is not None
    assert root.right is not None
    return 3 * magnitude(root.left) + 2 * magnitude(root.right)


def num_add(n1: Node, n2: Node) -> Node:
    assert n1 is not None
    assert n2 is not None
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

t_0 = time.time()
answer = parse(numbers[0])
for number in numbers[1:]:
    answer = num_add(answer, parse(number))
    reduce(answer)
answer = magnitude(answer)
print(f"Part 1: {answer}")
print(f"Elapsed in {time.time() - t_0:.02f} seconds")

t_0 = time.time()
answer = -1
for i, number1 in enumerate(numbers):
    for j, number2 in enumerate(numbers):
        if i == j:
            continue
        tmp = num_add(parse(number1), parse(number2))
        reduce(tmp)
        answer = max(answer, magnitude(tmp))

print(f"Part 2: {answer}")
print(f"Elapsed in {time.time() - t_0:.2f} seconds")

