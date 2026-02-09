from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def parse_file(filename) -> tuple(list[int], list[int]):
    l1, l2 = [], []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.split()
            if len(parts) == 2:
                l1.append(int(parts[0]))
                l2.append(int(parts[1]))
    return l1, l2

def solve1(filename):
    l1, l2 = parse_file(filename)
    l1.sort()
    l2.sort()

    total_dist = 0
    for elem1, elem2 in zip(l1,l2):
        total_dist += abs(elem1 - elem2)

    return total_dist

def solve2(filename):
    l1, l2 = parse_file(filename)

    c = Counter(l2)
    score = 0

    for elem in l1:
        mul_score = c.get(elem)
        # print(elem, mul_score)
        if mul_score:
            score += elem * mul_score 

    return score

def part1():
    expected = 11
    sol = solve1("sample.txt")
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")
    
    print(f"Solution Test: {solve1("input.txt")}")

def part2():
    expected = 31
    sol = solve2("sample.txt")
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")
    
    print(f"Solution Test: {solve2("input.txt")}")

if __name__ == "__main__":
    part1() # 1722302
    part2() # 20373490