from collections import defaultdict

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    @classmethod
    def from_list(cls, data):
        return cls(data[0], data[1])

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

def parse_file(filename):
    points = []
    with open(filename) as f:
        points = [ Point.from_list(line.strip().split(",")) for line in f.readlines() ]
    return points

def get_areas(points: list(Points)) -> list(tuple):
    pairs = []
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if i < j:
                area = (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)
                pairs.append((area, i, j))

    pairs.sort(key=lambda x: x[0], reverse=True)

    return pairs

def solve1(filename):
    points = parse_file(filename)
    pairs = get_areas(points)
    # print(pairs)
    # print(points[pairs[1][1]],points[pairs[1][2]])

    return pairs[0][0]

def solve2(filename):
    return 0

def part1():
    expected = 50
    sol = solve1("sample.txt")
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")
    
    print(f"Solution Test: {solve1("input.txt")}")

def part2():
    pass

if __name__ == "__main__":
    part1() # 4755278336
    # part2() # 