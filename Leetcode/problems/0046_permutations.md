# Leetcode 0046 - Permutations

## ✅ UMPIRE
- **Understand**: Return all possible permutations of the list `nums` (distinct integers)
- **Match**: Input is a list → suitable for backtracking
- **Plan**: Use DFS with backtracking and visited tracking
- **Implement**: See below
- **Review**: Check path building and backtrack step
- **Evaluate**: Time O(n!) due to all permutations, Space is O(n), due to the recursion depth, the path list, and the used array

---

## ✅ Metadata
- **Appears In**: Grind75
- **Pattern**: Backtracking (#7)
- **Data Structure**: Array, Boolean tracking list
- **Algorithm**: DFS, Recursion
- **Tags**: Backtracking, Recursion, DFS

---

## ✅ Solution Code

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    used[i] = False

        backtrack([])
        return res
```

---

## ✅ Trace (Interview-style Simulation)

```
backtrack([])
→ i=0: use 1 → path=[1]
  → i=1: use 2 → path=[1,2]
    → i=2: use 3 → path=[1,2,3] → ✅ add to res
    ← backtrack: pop 3
  ← backtrack: pop 2
  → i=2: use 3 → path=[1,3]
    → i=1: use 2 → path=[1,3,2] → ✅ add to res
    ← backtrack: pop 2
  ← backtrack: pop 3
← backtrack: pop 1

→ i=1: use 2 → path=[2]
  → i=0: use 1 → path=[2,1]
    → i=2: use 3 → path=[2,1,3] → ✅ add to res
    ← backtrack: pop 3
  ← backtrack: pop 1
  → i=2: use 3 → path=[2,3]
    → i=0: use 1 → path=[2,3,1] → ✅ add to res
    ← backtrack: pop 1
  ← backtrack: pop 3
← backtrack: pop 2

→ i=2: use 3 → path=[3]
  → i=0: use 1 → path=[3,1]
    → i=1: use 2 → path=[3,1,2] → ✅ add to res
    ← backtrack: pop 2
  ← backtrack: pop 1
  → i=1: use 2 → path=[3,2]
    → i=0: use 1 → path=[3,2,1] → ✅ add to res
    ← backtrack: pop 1
  ← backtrack: pop 2
← backtrack: pop 3

...
```

---

## ✅ Line-by-line Typing Script (English)

- I’m defining the permute function, which returns all permutations of the input list nums.
- I’m initializing res as an empty list to collect all valid permutations.
- This will be updated inside my recursive backtracking calls.
- It needs to be outside the recursive function so that it persists across all calls.
- Then I create a used array, initialized to False, to track which elements have already been added to the current path.
- Now I define the backtrack helper function — this is where I’ll build up the permutations recursively.
- If the path is already the same length as nums, it means we’ve formed a complete permutation.
- So I add a copy of the path to res, and return to explore other possibilities.
- Otherwise, I loop through all indices.
- If used[i] is False, I mark it as used, add nums[i] to the path, and call backtrack again to go deeper.
- After the recursive call returns, I perform the backtracking step: remove the last element from the path and reset used[i] to False.
- Finally, I call backtrack([]) to start the recursion with an empty path, and return the result list.