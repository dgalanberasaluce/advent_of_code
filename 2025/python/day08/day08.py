from collections import defaultdict

class Point:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    @classmethod
    def from_list(cls, data):
        return cls(data[0], data[1], data[2])

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

def squared_distance(p1:Point, p2:Point):
    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2


def solve1_bruteforce(filename, threshold):
    points = []
    distances = {}

    with open(filename) as f:
        for line in f.readlines():
            point = line.strip().split(",")
            p = Point.from_list(point)
            points.append(p)

    # --- Part 1: Calculate Distances ---
    # Calculate the distance from P1 to P2 for all points
    # We store: (squared_distance, idx1, idx2)
    pairs = []
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if i < j:
                dist_sq = squared_distance(p1, p2)
                pairs.append((dist_sq, i, j))

    # Sort by distance (smallest first)
    pairs.sort(key=lambda x: x[0])

    # --- Part 2: Find the circuits of junction boxes from the THRESHOLD shortest distances ---
    # Union-Find Data Structure Initialization
    parent = list(range(len(points)))

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    for _, idx_a, idx_b in pairs[:threshold]:
        union(idx_a, idx_b)
    
    # --- Part 3: Retrieve the size of each circuit ---
    # circuit_sizes = { idx_root_a -> size, idx_root_b -> size }
    circuit_sizes = defaultdict(int)

    for i in range(len(points)):
        root = find(i)
        circuit_sizes[root] += 1

    sizes = sorted(circuit_sizes.values(), reverse=True)

    # --- Part 4: Multiply the size of the 3 largest circuits ---
    ans = 1
    for size in sizes[:3]:
        ans *= size

    # --- (Optional) Retrieve the circuits ---
    # circuit_groups = defaultdict(list)
    # for i in range(len(points)):
    #     root = find(i)
    #     circuit_groups[root].append(points[i])
    # sorted_circuits = sorted(circuit_groups.values(), key=len, reverse=True)
    # print(f"--- Found {len(sorted_circuits)} distinct circuits ---\n")

    # for idx, group in enumerate(sorted_circuits, 1):
    #     print(f"Circuit #{idx} (Size: {len(group)}):")
    #     for p in group:
    #         print(f"  - {p}")
    #     print("")
    
    return ans


def solve1(filename, threshold = 10):
    return solve1_bruteforce(filename, threshold)

def part1():
    expected = 40
    sol = solve1("sample.txt")
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")
    
    print(f"Solution Test: {solve1("input.txt", 1000)}")

if __name__ == "__main__":
    part1() # 153328
    # part2()