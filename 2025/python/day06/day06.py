from itertools import zip_longest

def solve1(filename):

    with open(filename) as f:
        tmp_add = []
        tmp_mul = []
        tmp_ops = []

        for line in f:
            row = line.strip().split()

            if row[0] == "+" or row[0] == "*":
                tmp_ops = row
            else:
                tmp_add = [int(x) + int(y) for x, y in zip_longest(tmp_add, row, fillvalue=0)]
                tmp_mul = [int(x) * int(y) for x, y in zip_longest(tmp_mul, row, fillvalue=1)]
    
    ans = [ tmp_add[i] if op == "+" else tmp_mul[i] for i, op in enumerate(tmp_ops) ]
    return sum(ans)

def part1():
    expected = 4277556
    sol = solve1("sample.txt")
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")
    
    print(f"Solution Test: {solve1("input.txt")}")

if __name__ == "__main__":
    part1()