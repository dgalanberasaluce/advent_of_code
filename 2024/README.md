# Advent of Code 2024

| **Day** | **Part** | **Problem Description**                                                             | **Difficulty** | **Optimal Algorithm**                   | **Time / Space Complexity**                     |
|---------|----------|-------------------------------------------------------------------------------------|----------------|-----------------------------------------|-------------------------------------------------|
| 1       | 1        | Calculate distance between two sorted lists of location IDs.                        | Easy           | Sorting & Linear Scan                   | $O(N \log N)$ / $O(N)$                          |
|         | 2        | Calculate similarity score based on frequency of numbers in the second list.        | Easy           | Hash Map (Frequency Counter)            | $O(N)$ / $O(N)$                                 |
| 2       | 1        | Check if number sequences are strictly increasing/decreasing with limited steps.    | Easy           | Linear Scan (Window)                    | $O(N \times M)$ / $O(1)$                        |
|         | 2        | Check safety if one number can be removed ("Problem Dampener").                     | Easy           | Brute Force (Remove each index)         | $O(N \times M^2)$ / $O(M)$                      |
| 3       | 1        | Parse corrupted memory for valid mul(X,Y) instructions.                             | Easy           | Regex or String Parsing                 | $O(N)$ / $O(1)$                                 |
|         | 2        | Handle conditional do() and don't() instructions enabling/disabling multiplication. | Easy           | Finite State Machine (Linear Scan)      | $O(N)$ / $O(1)$                                 |
| 4       | 1        | Find word "XMAS" in a grid in 8 directions.                                         | Medium         | Grid Traversal (Direction Vectors)      | $O(W \times H)$ / $O(1)$                        |
|         | 2        | Find "X-MAS" crosses (two "MAS" intersecting).                                      | Medium         | Pattern Matching (3x3 Kernel)           | $O(W \times H)$ / $O(1)$                        |
| 5       | 1        | Validate page ordering updates against prerequisite rules.                          | Medium         | Hash Map / Set Lookup                   | $O(N \times M)$ / $O(R)$                        |
|         | 2        | Reorder invalid updates to satisfy rules.                                           | Medium         | Topological Sort or Custom Comparator   | $O(M \log M)$ / $O(M)$                          |
| 6       | 1        | Simulate a guard's distinct path in a grid until they leave.                        | Medium         | Simulation (Grid Walk)                  | $O(W \times H)$ / $O(W \times H)$               |
|         | 2        | Add one obstacle to create a loop.                                                  | Medium         | Simulation (Brute Force) or Graph Jump  | $O((W \times H)^2)$ / $O(W \times H)$           |
| 7       | 1        | Check if equations can be true using + and * operators.                             | Medium         | Recursion / DFS                         | $O(2^N)$ / $O(N)$                               |
|         | 2        | Include concatenation operator \|\|.                                                | Medium         | Recursion / DFS                         | $O(3^N)$ / $O(N)$                               |
| 8       | 1        | Find antinodes based on antenna pairs and distance reflection.                      | Easy           | Vector Arithmetic (Pairwise Iteration)  | $O(A^2)$ / $O(W \times H)$                      |
|         | 2        | Find antinodes at all harmonic positions along the line.                            | Medium         | Line Drawing (GCD Steps)                | $O(A^2 \times \max(W,H))$ / $O(W \times H)$     |
| 9       | 1        | Compact disk blocks by moving files to leftmost free space.                         | Medium         | Two Pointers                            | $O(N)$ / $O(N)$                                 |
|         | 2        | Move whole files to leftmost sufficient span (defrag).                              | Hard           | Doubly Linked List or Heaps for gaps    | $O(N \log N)$ / $O(N)$                          |
| 10      | 1        | Find reachable summits (9) from trailheads (0) on a topo map.                       | Easy           | BFS / DFS (Reachability)                | $O(N)$ / $O(N)$                                 |
|         | 2        | Count distinct hiking trails (ratings).                                             | Medium         | DFS with Memoization or DP              | $O(N)$ / $O(N)$                                 |
| 11      | 1        | Simulate stone splitting rules for 25 blinks.                                       | Easy           | Simulation (List/Vector)                | $O(2^{25})$ / $O(2^{25})$                       |
|         | 2        | Simulate stone splitting for 75 blinks (exponential growth).                        | Medium         | Dynamic Programming (Counter Map)       | $O(U \times \text{Steps})$ / $O(U)$             |
| 12      | 1        | Calculate fence price (Area $\times$ Perimeter) for regions.                        | Medium         | BFS / Flood Fill                        | $O(W \times H)$ / $O(W \times H)$               |
|         | 2        | Calculate fence price (Area $\times$ Number of Sides).                              | Hard           | Corner Counting (Geometry)              | $O(W \times H)$ / $O(W \times H)$               |
| 13      | 1        | Find min tokens to win claw machine (linear combinations).                          | Easy           | Brute Force                             | $O(1)$ / $O(1)$                                 |
|         | 2        | Inputs offset by $10^{13}$; brute force impossible.                                 | Medium         | Linear Algebra (Cramer's Rule)          | $O(1)$ / $O(1)$                                 |
| 14      | 1        | Predict robot positions after 100 seconds (wrapping grid).                          | Easy           | Modular Arithmetic                      | $O(N)$ / $O(1)$                                 |
|         | 2        | Find the second where robots form a Christmas Tree.                                 | Hard           | Variance Minimization / Visual Search   | $O(T \times N)$ / $O(1)$                        |
| 15      | 1        | Simulate warehouse robot pushing boxes (Sokoban).                                   | Medium         | Simulation                              | $O(M \times D)$ / $O(W \times H)$               |
|         | 2        | Boxes become wide []; pushing affects multiple columns.                             | Hard           | Recursive Check & Commit                | $O(M \times D^2)$ / $O(W \times H)$             |
| 16      | 1        | Find lowest score path in maze (move=1, turn=1000).                                 | Medium         | Dijkstra's Algorithm                    | $O(E \log V)$ / $O(V)$                          |
|         | 2        | Count all tiles that are part of any optimal path.                                  | Hard           | Bidirectional Dijkstra / Backtracking   | $O(E \log V)$ / $O(V)$                          |
| 17      | 1        | Run a 3-bit computer program.                                                       | Medium         | Simulation                              | $O(N)$ / $O(1)$                                 |
|         | 2        | Find initial register A that outputs the program itself (Quine).                    | Very Hard      | Reverse Engineering / DFS (Octal)       | $O(4^K)$ / $O(K)$                               |
| 18      | 1        | Find shortest path after $N$ bytes fall.                                            | Easy           | BFS                                     | $O(W \times H)$ / $O(W \times H)$               |
|         | 2        | Find the first byte that makes the exit unreachable.                                | Medium         | Binary Search + BFS                     | $O(W \times H \times \log N)$ / $O(W \times H)$ |
| 19      | 1        | Check if towel designs can be made from patterns.                                   | Medium         | Recursion / Trie                        | $O(N \times L)$ / $O(L)$                        |
|         | 2        | Count total number of ways to make each design.                                     | Medium         | Dynamic Programming / Memoization       | $O(N \times L)$ / $O(L)$                        |
| 20      | 1        | Find cheats (shortcuts) passing through walls (length 2).                           | Medium         | BFS + Manhattan Dist Check              | $O(P)$ / $O(W \times H)$                        |
|         | 2        | Find cheats of length up to 20.                                                     | Hard           | BFS + Window Search                     | $O(P \times C^2)$ / $O(W \times H)$             |
| 21      | 1        | Control robot arms on nested keypads (Depth 2).                                     | Hard           | BFS (Shortest Path)                     | $O(S^D)$ / $O(S)$                               |
|         | 2        | Control robot arms on nested keypads (Depth 25).                                    | Very Hard      | DP with Memoization (Split by 'A')      | $O(N \times D)$ / $O(1)$                        |
| 22      | 1        | Simulate secret number evolution (PRNG).                                            | Easy           | Bitwise Operations                      | $O(N \times S)$ / $O(1)$                        |
|         | 2        | Find sequence of 4 price changes maximizing bananas.                                | Medium         | Sliding Window + Hash Map               | $O(N \times S)$ / $O(S)$                        |
| 23      | 1        | Find sets of 3 inter-connected computers (Triangles).                               | Medium         | Graph Traversal (Adjacency List)        | $O(V + E)$ / $O(V+E)$                           |
|         | 2        | Find the largest group of fully connected computers (Clique).                       | Hard           | Bron-Kerbosch Algorithm                 | $O(3^{V/3})$ / $O(V+E)$                         |
| 24      | 1        | Simulate logic gates (AND, XOR, OR).                                                | Easy           | Topological Sort / Recursion            | $O(N)$ / $O(N)$                                 |
|         | 2        | Fix the swapped wires in the Ripple Carry Adder.                                    | Very Hard      | Structural Verification (Pattern Match) | $O(N)$ / $O(1)$                                 |
| 25      | 1        | Fit keys into locks (schematic overlap).                                            | Easy           | Matrix/Vector Comparison                | $O(K \times L)$ / $O(1)$                        |
|         | 2        | Deliver the Chronicle (Click the button).                                           | Free           | Completion (50 Stars required)          | N/A                                             |

**Key to Abbreviations**
- DP: Dynamic Programming
- BFS: Breadth-First Search
- DFS: Depth-First Search
- CRT: Chinese Remainder Theorem
- $U$: Number of unique stone values (Day 11)
- $P$: Length of path (Day 20)
- $C$: Cheat duration (Day 20)