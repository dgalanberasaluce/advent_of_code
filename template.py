def solve1(filename):
    with open(filename) as f:
        line = f.readlines().strip()
    return -1

def solve2(filename):
    pass

def part1():
    expected = 0
    sol = solve1("sample.txt")
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")
    
    print(f"Solution Test: {solve1("input.txt")}")

def part2():
    expected = 0
    sol = solve2("sample.txt")
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")
    
    print(f"Solution Test: {solve2("input.txt")}")

if __name__ == "__main__":
    part1() # 
    # part2() # 