import re


def parse_file(filename) -> list[list[str]]:
    text = ""
    with open(filename, "r") as f:
        for line in f:
            text += line.strip()
    return text


def solve1(filename):
    text = parse_file(filename)
    pattern = r"mul\(([\d]+),([\d]+)\)"
    ops = re.findall(pattern, text)

    ans = sum([int(elem[0]) * int(elem[1]) for elem in ops])

    return ans


def solve2(filename):
    pass


def part1():
    expected = 161
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

    # print(f"Solution Test: {solve2("input.txt")}")


if __name__ == "__main__":
    part1()  # 166630675
    # part2()  #
