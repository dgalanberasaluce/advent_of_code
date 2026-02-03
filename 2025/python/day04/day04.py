import time

def _has_a_roll(m,i,j):
    if i == -1 or i == len(m) or j == -1 or j == len(m[0]):
        return 0
    
    return 1 if m[i][j] == '@' else 0

def solve1(m):
    can_access = 0
    for row in range(len(m)):
        for column in range(len(m[0])):
            if _has_a_roll(m,row,column):
                if sum([
                    _has_a_roll(m,row-1,column-1),
                    _has_a_roll(m,row-1,column),
                    _has_a_roll(m,row-1,column+1),
                    _has_a_roll(m,row,column-1),
                    _has_a_roll(m,row,column+1),
                    _has_a_roll(m,row+1,column-1),
                    _has_a_roll(m,row+1,column),
                    _has_a_roll(m,row+1,column+1),]
                ) < 4:
                    can_access += 1
    return can_access         

"""
    Solution in O(N x K)
"""
def solve2(m):
    total_rolls = 0

    while True:
        removals = []

        rolls_to_remove = 0
        for row in range(len(m)):
            for column in range(len(m[0])):
                if _has_a_roll(m,row,column):
                    if sum([
                        _has_a_roll(m,row-1,column-1),
                        _has_a_roll(m,row-1,column),
                        _has_a_roll(m,row-1,column+1),
                        _has_a_roll(m,row,column-1),
                        _has_a_roll(m,row,column+1),
                        _has_a_roll(m,row+1,column-1),
                        _has_a_roll(m,row+1,column),
                        _has_a_roll(m,row+1,column+1),]
                    ) < 4:
                        removals.append((row,column))
        
        if not removals:
            break

        for r, c in removals:
            m[r][c] = "x"

        total_rolls += len(removals)

    return total_rolls

"""
    Solution in O(N)

    Description = Chain reaction (implemented as a Propagation Queue) is a pattern used to solve problems
    where a change in one element causes changes in its neighbors

    The algorithm:
    1. Find the initial "trigger" and put it into a Queue (or Stack)
    2. Prcessing: Pull an item from the queue
    3. Update: Change the state of that item (e.g. mark it as "removed")
    4. Notification: look at the neighbors of that item. If the item is affected by the change, add that neighbor to the queue
    5. Repeat: Continue until the queue is empty
"""
def solve2_opt(m):
    rows = len(m)
    cols = len(m[0])

    counts = [[0] * cols for _ in range(rows)]
    stack = []

    # position of neighbors
    deltas = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

    # Initial scan
    for r in range(rows):
        for c in range(cols):
            if m[r][c] == "@":
                cnt = 0
                for dr, dc in deltas:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and m[nr][nc] == '@':
                        cnt += 1
                counts[r][c] = cnt

                if cnt < 4:
                    stack.append((r, c))
        total_removed = 0

    while stack:
        r, c = stack.pop()
        if m[r][c] != "@":
            continue

        m[r][c] = 'x'
        total_removed += 1

        for dr, dc in deltas:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and m[nr][nc] == '@':
                counts[nr][nc] -= 1

                if counts[nr][nc] == 3:
                    stack.append((nr, nc))
    return total_removed

def prepare(filename):
    m = []
    with open(filename) as f:
        for line in f:
            m.append(list(line.strip()))
    return m

def part1():
    expected = 13
    m = prepare("sample.txt")
    sol = solve1(m)
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")
    print(f"Solution Test: {solve1(prepare("input.txt"))}")

def part2():
    expected = 43
    m = prepare("sample.txt")
    sol = solve2(m)
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")
    print(f"Solution Test: {solve2(prepare("input.txt"))}")

def part2_t():
    m = prepare("input.txt")
    start_time = time.time()
    print(solve2(prepare("input.txt")))
    print("No optimized version: %s" % (time.time() - start_time))

def part2_opt_t():
    m = prepare("input.txt")
    start_time = time.time()
    print(solve2_opt(prepare("input.txt")))
    print("Optimized version: %s" % (time.time() - start_time)) 

if __name__ == "__main__":
    part1()
    part2()
    part2_t()
    part2_opt_t()
