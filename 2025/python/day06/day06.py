def solve1(filename):
    with open(filename) as f:
        lines = f.readlines()

    ops = lines[len(lines)-1].strip().split()
    acc = [0 if op == "+" else 1 for op in ops]

    for line in lines[:-1]:
        row = line.strip().split()

        for i, val in enumerate(row):
            if i >= len(ops): break
            
            num = int(val)
            if ops[i] == "+":
                acc[i] += num
            else:
                acc[i] *= num
                
    return sum(acc)

def part1():
    expected = 4277556
    sol = solve1("sample.txt")
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")
    
    print(f"Solution Test: {solve1("input.txt")}")

if __name__ == "__main__":
    part1() # 5381996914800