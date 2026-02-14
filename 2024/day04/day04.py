def parse_file(filename) -> list[str]:
    grid = []
    with open(filename, "r") as f:
        for line in f:
            grid.append(line.strip())

    return grid


def solve1(filename):
    grid = parse_file(filename)
    rows, cols = len(grid), len(grid[0])
    target = "XMAS"
    count = 0
    directions = [(dr, dc) for dr in [-1, 0, 1] for dc in [-1, 0, 1] if dr or dc]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "X":
                for dr, dc in directions:
                    if 0 <= r + dr * 3 < rows and 0 <= c + dc * 3 < cols:
                        if all(
                            grid[r + i * dr][c + i * dc] == target[i]
                            for i in range(1, 4)
                        ):
                            count += 1

    return count


def solve2(filename):
    grid = parse_file(filename)
    rows, cols = len(grid), len(grid[0])
    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "A":
                if 0 < r < rows - 1 and 0 < c < cols - 1:
                    # Store corners in a set. Set removes duplicates
                    # Two Set are equal if it contains the same elements
                    diag1 = {grid[r - 1][c - 1], grid[r + 1][c + 1]}
                    diag2 = {grid[r - 1][c + 1], grid[r + 1][c - 1]}

                    if diag1 == {"M", "S"} and diag2 == {"M", "S"}:
                        count += 1

    return count


def part1():
    expected = 18
    sol = solve1("sample.txt")
    print(
        f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}"
    )

    print(f"Solution Test: {solve1("input.txt")}")


def part2():
    expected = 9
    sol = solve2("sample.txt")
    print(
        f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}"
    )

    print(f"Solution Test: {solve2("input.txt")}")


if __name__ == "__main__":
    part1()  # 2458
    part2()  # 1945
