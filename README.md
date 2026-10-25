# Algo Trainer - a LeetCode-style practice environment for VS Code

19 sections · 125+ problems · 470+ tests · lessons + reference solutions.
Built for interview and online-assessment prep (e.g. the Turing algorithms test).

## 1. Setup (2 minutes)
```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
code .                             # open the folder in VS Code
```
VS Code: install the **Python** extension, then `Ctrl+Shift+P` → *Python: Select Interpreter* → pick `.venv`.
Open the **Testing** panel (beaker icon). Every problem shows up as a test you can run or **debug** with a click.

## 2. The learning loop
For each section, in order:
1. **Read** `sections/NN_name/lesson.md` (10-15 min).
2. **Open** `sections/NN_name/problems.py`. Each function has a docstring with the task, an example and a target complexity. Replace `pass` with your solution.
3. **Run the tests** - Testing panel, or the terminal:
   ```bash
   python run.py 3             # run section 03 against YOUR code
   python run.py list          # progress for all sections
   python run.py all           # everything
   ```
4. **Stuck?** Think 15-20 min, then read the hints in the lesson, *then* peek at `solutions/NN_name.py`.
   Check a solution against the tests with `python run.py 3 --solutions`.
5. **Re-do** problems you needed hints for, 2-3 days later, from scratch (`python run.py reset 3` wipes a section back to blank stubs).

Debugging a failing test: set a breakpoint in your function and click the Debug icon next to the test in the Testing panel.
Each test has a 10-second timeout (catches infinite loops and too-slow solutions).

## 3. Curriculum
| # | Section | Core ideas |
|---|---|---|
| 01 | Arrays & Hashing | Big-O, hash maps, counting, prefix/suffix products |
| 02 | Two Pointers | converging, slow/fast, 3Sum, rain water |
| 03 | Sliding Window | fixed & variable windows |
| 04 | Prefix Sums & Intervals | range sums, subarray-sum maps, merge, sweep line |
| 05 | Stacks | brackets, RPN, monotonic stack, histogram |
| 06 | Binary Search | lower bound, rotated arrays, search on the answer |
| 07 | Linked Lists | dummy head, reverse, Floyd, gap pointers |
| 08 | Trees | DFS/BFS, BST validation, LCA, diameter, path sum |
| 09 | Heaps | top-k, two heaps, k-way merge, scheduling |
| 10 | Graph Traversal | DFS/BFS, grids, multi-source BFS, bipartite, word ladder |
| 11 | Advanced Graphs | topo sort, union-find, Dijkstra, MST, Bellman-Ford |
| 12 | Backtracking | subsets, permutations, combinations, N-Queens |
| 13 | DP 1-D | stairs, robber, coins, LIS, word break, decode ways |
| 14 | DP 2-D | grids, LCS, edit distance, knapsack, state machines |
| 15 | Greedy | Kadane, jumps, intervals, gas station |
| 16 | Bits & Math | XOR, masks, sieve, gcd, fast power |
| 17 | Sorting | merge/quick/heap sort, quickselect, inversions |
| 18 | Tries & Strings | trie, wildcard search, KMP, palindromes |
| 19 | Advanced Structures | LRU, Fenwick, segment tree, monotonic deque |

**Suggested pace:** 1-2 sections per day = about 2 weeks. If short on time, do 01-08, 10, 12, 13, 15 first (the most common test topics), then the rest.

## 4. Test-day habits
- Read the constraints → they tell you the target complexity (see `CHEATSHEET.md`).
- Write the brute force first, then optimise. Partial credit beats nothing.
- Test edge cases: empty, one element, duplicates, negatives, max size.
- Say the complexity of your solution out loud before submitting.
- Time-box: if a problem eats 20+ minutes, move on and come back.

## Project layout
```
sections/NN_name/lesson.md        teaching notes
sections/NN_name/problems.py      YOUR workspace (stubs)
sections/NN_name/test_problems.py tests (don't edit)
solutions/NN_name.py              reference solutions + commentary
helpers.py                        ListNode, TreeNode, builders, loader
run.py                            tiny CLI (list / run / reset)
tools/make_stubs.py               regenerates blank stubs from solutions
```
Note: a few in-place problems (e.g. `sort_colors` on already-sorted input) pass trivially even when empty - that is expected; the real tests are the rest of the section.
