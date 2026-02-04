import bisect
import time

def solve1(fresh_ingredients_range, avail):
    acc = 0

    for elem in avail:
        for r in fresh_ingredients_range:
            if r[0] <= elem <= r[1]:
                acc += 1
                break
    return acc

def solve1_opt(r_opt, avail):

    start_points = [r[0] for r in r_opt]
    fresh_count = 0

    for val in avail:
        idx = bisect.bisect_right(start_points, val) - 1

        if idx >= 0:
            range_start, range_end = r_opt[idx]
            if range_start <= val <= range_end:
                fresh_count += 1
    
    return fresh_count

def solve2(ingredient_ranges):
    sorted_ranges = sorted(ingredient_ranges)

    if not sorted_ranges:
        return 0

    merged_intervals = []
    merged_intervals.append(sorted_ranges[0])
    active_start, active_end = sorted_ranges[0]

    for next_start, next_end in sorted_ranges[1:]:

        if next_start <= active_end:
            if active_end < next_end:
                merged_intervals[-1] = (active_start, next_end)
                active_end = next_end
        else:
            merged_intervals.append((next_start, next_end))
            active_start, active_end = next_start, next_end

    total_coverage_count = 0
    previous_interval_end = 0

    for start, end in merged_intervals:
        range_size = end - start + 1
        total_coverage_count += range_size
        previous_interval_end = end
    
    return total_coverage_count

def solve2_opt(ingredient_ranges):
    sorted_ranges = sorted(ingredient_ranges)

    if not sorted_ranges:
        return 0
    
    total_coverage = 0

    current_start, current_end = sorted_ranges[0]

    for next_start, next_end in sorted_ranges[1:]:
        if next_start <= current_end:
            current_end = max(current_end, next_end)
        else:
            total_coverage += (current_end - current_start + 1)
            current_start, current_end = next_start, next_end

    # Add the final range
    total_coverage += (current_end - current_start + 1)
    
    return total_coverage


def get_optimized_range(fresh_ingredients_range):
    sorted_range = sorted(fresh_ingredients_range, key=lambda x: x[0])
    merged_ranges = []

    curr_start, curr_end = sorted_range[0]
    for i in range(1, len(sorted_range)):
        next_start, next_end = sorted_range[i]

        if next_start <= curr_end + 1:
            curr_end = max(curr_end, next_end)
        else:
            merged_ranges.append((curr_start, curr_end))
            curr_start, curr_end = next_start, next_end
        merged_ranges.append((curr_start, curr_end))

    return merged_ranges

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

def part1_t():
    start_time = time.time()
    r, avail = pre("input.txt")
    sol = solve1(r,avail)
    print(f"Time part1: {time.time() - start_time}")

def part1_opt_t():
    start_time = time.time()
    r, avail = pre("input.txt")
    r_opt = get_optimized_range(r)
    sol = solve1_opt(r_opt, avail)
    print(f"Time part1 optimized: {time.time() - start_time}")

def part2():
    expected = 14
    r, avail = pre("sample.txt")
    sol = solve2(r)
    print(f"{"PASS" if expected == sol else "FAILED"} solution: {sol} - expected: {expected}")

    r, avail = pre("input.txt")
    start_time = time.time()
    sol = solve2(r)
    end_time = time.time()
    print(f"Solution Test Optimized: {sol} ({end_time - start_time} s)")

    start_time = time.time()
    sol = solve2_opt(r)
    end_time = time.time()
    print(f"Solution Test Optimized: {sol} ({end_time - start_time} s)")


if __name__ == "__main__":
    part1()
    part1_t()
    part1_opt_t()
    part2()
