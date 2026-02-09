def parse_file(filename) -> list[list[str]]:
    reports = []
    with open(filename) as f:
        for line in f:
            levels = line.split()
            reports.append(levels)
    return reports

def solve1_opt(filename):
    reports = parse_file(filename)
    safe_reports = 0

    for report in reports:
        diffs = [int(b) - int(a) for a,b in zip(report, report[1:])]
        if all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs):
            safe_reports += 1

    return safe_reports

def solve1(filename):
    reports = parse_file(filename)
    unsafe_reports = 0

    for report in reports:
        level_state = None
        for pos, elem in enumerate(report[1:]):

            diff = int(elem) - int(report[pos])

            if diff == 0:
                unsafe_reports += 1
                break

            state = 1 if diff > 0 else -1

            if abs(diff) > 3 or (level_state is not None and level_state != state):
                unsafe_reports += 1
                break
            
            level_state = state
        

    return len(reports) - unsafe_reports

def solve2(filename):
    pass

def part1():
    expected = 2
    sol = solve1("sample.txt")
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")
    
    print(f"Solution Test: {solve1("input.txt")}")

def part2():
    expected = 4
    sol = solve2("sample.txt")
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")
    
    print(f"Solution Test: {solve2("input.txt")}")

if __name__ == "__main__":
    part1() # 402
    # part2() # 