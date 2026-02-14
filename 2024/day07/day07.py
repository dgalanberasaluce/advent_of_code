class NodeTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def parse_file(filename: str) -> list[tuple[int, list[int]]]:
    parsed = []
    with open(filename, "r") as f:
        for line in f:
            target_str, nums_str = line.split(":")
            target = int(target_str)
            nums = [int(n) for n in nums_str.split()]

            parsed.append((target, nums))

    return parsed


def check_valid(nums, target):
    def dfs(index, current_val):
        if index == len(nums):
            return current_val == target
        return dfs(index + 1, nums[index] + current_val) or dfs(
            index + 1, nums[index] * current_val
        )

    return dfs(1, nums[0])


def solve1(filename):
    parsed = parse_file(filename)

    ans = 0
    for target, nums in parsed:
        if check_valid(nums, target):
            ans += target

    # Pythonic
    # ans = sum(target for target, nums in parsed if check_valid(nums, target))

    return ans


def solve2(filename):
    pass


def part1():
    expected = 3749
    sol = solve1("sample.txt")
    print(
        f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}"
    )

    print(f"Solution Test: {solve1("input.txt")}")


def part2():
    expected = -1
    sol = solve2("sample.txt")
    print(
        f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}"
    )

    print(f"Solution Test: {solve2("input.txt")}")


if __name__ == "__main__":
    part1()  # 2437272016585
    # part2()  #
