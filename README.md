# Advent of code

>[!NOTE]
> _Advent of Code (AoC) is an annual series of holiday-themed programming puzzles that run every December_
>
>_https://adventofcode.com/_


# Cheatsheet
## Python

**Buil-int Functions**
- `zip(*matrix)`: Transpose a 2D matrix instantly
```python
print(tuple(zip((1,2),(3,4)))) # ((1,3),(2,4))
```
- `enumerate(arr)`: Get index and value simultaneously
```python
for pos, elem in enumerate(my_arr):
  print(pos, elem)
```
- `sorted(arr, key=...)`: Custom sorting. Returns a new list (vs `arr.sort()`)
```python
l = [(5,10), (21, 3)]
# Sort by the second element
sorted(l, key=lambda x: x[1]) # [(21, 3), (5, 10)]
```

**Imported Functions**
```python
import collections
import heapq
import bisect

# --- collections ---
counts = Counter(<iterable-or-mapping>) # Count occurrences
counts.total()

d = collections.defaultdict(<default_value_type>)
d = collections.defaultdict()        # defaultdict(None, {})
dl = collections.defaultdict(list)   # defaultdict(<class 'list'>, {})

# LIFO queue
q = collections.deque([1,2,3,4,5])
q.pop()     # 5
q.popleft() # 1

# --- heapq --- (Min-Heap by default, use negative keys for Max-Heap)
h = heapq.heapify(list) # Converts list to heap

# -- bisect --- (Binary search)
bisect.bisect_left(arr, x)
bisect.bisect_right(arr, x)
```

**Utils/shortcuts**
- List Comprehension `[ x for x in range(10) if x % 2 == 0 ]`
- `import sys; input = sys.stdin.readline.sptrip()`
- `sys.stdin.read().split()`: Read the entire file into memory at once

**Checking if a List is `None` vs empty**
```python
# Check if list exists and has elements
if my_list:

# Check specifically for None
if my_list is None:

# Check if list is empty
if not my_list:          # Works for all collections
if len(my_list) == 0:
if my_list == []:
```
