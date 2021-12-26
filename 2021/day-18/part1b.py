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

    def split(self) -> None:
        fst, snd = self.value // 2, (self.value + 1) // 2
        self.value = None
        self.left = Node(fst, None, None, self)
        self.right = Node(snd, None, None, self)

    def explode(self) -> tuple[int]:
        assert self.left.value is not None
        assert self.right.value is not None
        fst, snd = self.left.value, self.right.value
        self.value = 0
        self.left = None
        self.right = None
        return (fst, snd)


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


def parse(string: str) -> Node:
    if string[0] != '[':
        return Node(int(string))
    result = Node()
    current = ''
    count = 0
    for letter in string[1:-1]:
        if letter == '[':
            current += letter
            count += 1
        elif letter == ']':
            current += letter
            count -= 1
        elif (letter == ',') and \
             (count == 0):
            result.left = parse(current)
            result.left.parent = result
            current = ''
        else:
            current += letter
    if current != '':
        result.right = parse(current)
        result.right.parent = result
    return result


def add_to_left(val, node: Node) -> None:
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


def add_to_right(val, node: Node) -> None:
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
            fst, snd = root.explode()
            add_to_left(fst, root)
            add_to_right(snd, root)
            return True
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
            root.split()
            return True
        return False
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
answer: int = -1
for i, number1 in enumerate(numbers):
    for j, number2 in enumerate(numbers):
        if i == j:
            continue
        tmp = num_add(parse(number1), parse(number2))
        reduce(tmp)
        answer = max(answer, magnitude(tmp))

print(f"Part 2: {answer}")
print(f"Elapsed in {time.time() - t_0:.2f} seconds")
