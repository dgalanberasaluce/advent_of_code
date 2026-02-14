import math


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


def check_valid_concat(nums, target):
    def dfs(index, current_val):
        if current_val > target:  # Optimization: Pruning
            return False

        if index == len(nums):
            return current_val == target

        # n_digits = len(str(nums[index]))
        n_digits = int(math.log10(nums[index])) + 1

        return (
            dfs(index + 1, nums[index] + current_val)
            or dfs(index + 1, nums[index] * current_val)
            or dfs(index + 1, nums[index] + current_val * 10**n_digits)
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
    parsed = parse_file(filename)

    ans = 0
    for target, nums in parsed:
        if check_valid_concat(nums, target):
            ans += target
        # else:
        # print(nums, target)
    return ans


def part1():
    expected = 3749
    sol = solve1("sample.txt")
    print(
        f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}"
    )

    print(f"Solution Test: {solve1("input.txt")}")


def part2():
    expected = 11387
    sol = solve2("sample.txt")
    print(
        f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}"
    )

    print(f"Solution Test: {solve2("input.txt")}")


if __name__ == "__main__":
    part1()  # 2437272016585
    part2()  # 162987117690649
