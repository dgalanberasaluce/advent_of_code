# Day 07

**Part 1**

Pre:
- Order of evaluation is from left to right
- Numbers remain in the given order

Steps:
- Build a Decision Tree
- Depth-First Search Pattern

1. Start Recursion at Index 1
2. Recursively calculate sum and mul of current_index and accumulated
3. If index is equal to lenth of nums, then check if the accumulated is equal to the target
