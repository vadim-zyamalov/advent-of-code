from itertools import combinations


def search_wrong(nums, n=25):
    N = len(nums)
    assert N > n, "insufficient number of numbers"

    for i in range(n, N):
        if not any((n0 + n1 == nums[i]) for n0, n1 in combinations(nums[i - n : i], 2)):
            return nums[i]

    return None


def search_seq(nums, num):
    i, j = 0, 1
    sseq = nums[0]

    while sseq != num:
        if sseq < num:
            sseq += nums[j]
            j += 1
        elif sseq > num:
            sseq -= nums[i]
            i += 1

    return i, j


if __name__ == "__main__":
    with open("_inputs/2020/day-09/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split("\n")))

        wrong = search_wrong(numbers, 25)
        print(f"Part 1: {wrong}")

        i, j = search_seq(numbers, wrong)
        print(f"Part 2: {min(numbers[i:j]) + max(numbers[i:j])}")
