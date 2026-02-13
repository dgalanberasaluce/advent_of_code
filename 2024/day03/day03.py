import re


def parse_file(filename):
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
    text = parse_file(filename)
    pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"

    matches = re.finditer(pattern, text)

    total_sum = 0
    enabled = True  # At the beginning of the program, mul instructions are enabled

    for match in matches:
        token = match.group(0)

        if token == "do()":
            enabled = True
        elif token == "don't()":
            enabled = False
        elif token.startswith("mul"):
            if enabled:
                x = int(match.group(1))
                y = int(match.group(2))
                total_sum += x * y

    return total_sum


def part1():
    expected = 161
    sol = solve1("sample.txt")
    print(
        f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}"
    )

    print(f"Solution Test: {solve1("input.txt")}")


def part2():
    expected = 48
    sol = solve2("sample2.txt")
    print(
        f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}"
    )

    print(f"Solution Test: {solve2("input.txt")}")


if __name__ == "__main__":
    part1()  # 166630675
    part2()  # 93465710
