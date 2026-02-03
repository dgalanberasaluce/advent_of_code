def solve1(fresh_ingredients_range, avail):
    acc = 0

    for elem in avail:
        for r in fresh_ingredients_range:
            if r[0] <= elem <= r[1]:
                acc += 1
                break
    return acc


def pre(filename):
    fresh_ingredients_range = []
    available_ingredient_ids = []

    with open(filename, 'r') as f:
        for line in f.readlines():
            if '-' in line:
                l, r = (int(x) for x in line.split("-"))
                fresh_ingredients_range.append((l,r))
            elif not line.strip():
                continue
            else:
                available_ingredient_ids.append(int(line))
            
    return fresh_ingredients_range, available_ingredient_ids

def part1():
    expected = 3
    r, avail = pre("sample.txt")
    sol = solve1(r, avail)
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")
    
    r, avail = pre("input.txt")
    print(f"Solution Test: {solve1(r, avail)}")

if __name__ == "__main__":
    part1()