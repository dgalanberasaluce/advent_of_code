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

class DSU():
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False
    
    def get_all_sets(self):
        from collections import defaultdict
        sets = defaultdict(list)

        for i in range(len(self.parent)):
            root = self.find(i)
            sets[root].append(i)
        
        return dict(sets)

def squared_distance(p1:Point, p2:Point):
    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2

def get_points(filename: str) -> list(Points):
    points = []
    with open(filename) as f:
        for line in f.readlines():
            point = line.strip().split(",")
            p = Point.from_list(point)
            points.append(p)

    return points

# --- Part 1: Calculate Distances ---
# Calculate the distance from P1 to P2 for all points
# We store: (squared_distance, idx1, idx2)
def get_distances(points: list(Points)) -> list(tuple):
    pairs = []
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if i < j:
                dist_sq = squared_distance(p1, p2)
                pairs.append((dist_sq, i, j))

    # Sort by distance (smallest first)
    pairs.sort(key=lambda x: x[0])

    return pairs

def solve1_bruteforce(filename, threshold):
    points = get_points(filename)
    pairs = get_distances(points)

    # --- Part 2: Find the circuits of junction boxes from the THRESHOLD shortest distances ---
    # Union-Find Data Structure Initialization
    dsu = DSU(len(points))

    for _, idx_a, idx_b in pairs[:threshold]:
        dsu.union(idx_a, idx_b)
    
    # --- Part 3: Retrieve the size of each circuit ---
    # circuit_sizes = { idx_root_a -> size, idx_root_b -> size }
    circuit_sizes = defaultdict(int)

    for i in range(len(points)):
        root = dsu.find(i)
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

def solve2_bruteforce(filename):
    points = get_points(filename)
    pairs = get_distances(points)

    # --- Part 2: Find the circuits of junction boxes from the THRESHOLD shortest distances ---
    # Union-Find Data Structure Initialization
    dsu = DSU(len(points))

    last_idx_a, last_idx_b = 0, 0
    for _, idx_a, idx_b in pairs:
        if dsu.union(idx_a, idx_b):
            last_idx_a, last_idx_b = idx_a, idx_b

    return points[last_idx_a].x * points[last_idx_b].x

def solve1(filename, threshold = 10):
    return solve1_bruteforce(filename, threshold)

def solve2(filename):
    return solve2_bruteforce(filename)

def part1():
    expected = 40
    sol = solve1("sample.txt")
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")
    
    print(f"Solution Test: {solve1("input.txt", 1000)}")

def part2():
    expected = 25272
    sol = solve2("sample.txt")
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")
    
    print(f"Solution Test: {solve2("input.txt")}")

if __name__ == "__main__":
    part1() # 153328
    part2() # 6095621910