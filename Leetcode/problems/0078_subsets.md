
# Leetcode 0078 - Subsets

## ☀️ UMPIRE

- **Understand**: Return all possible subsets (the power set) of a list "nums" with distinct integers.
- **Match**: This is a classic combinatorial problem → fits backtracking pattern.
- **Plan**: Use backtracking with "start" to generate combinations and avoid duplicates.
- **Implement**: Recurse by adding current path to result, explore new choices from current index forward, and backtrack.
- **Review**: Include empty set, full set, and ensure no element is reused in the same path.
- **Evaluate**:
- **Time**: O(2^n * n) → 2^n subsets × O(n) copy time
- **Space**: O(n) recursion + O(2^n * n) result



## ☀️ Metadata

- **Appears In**: Grind75
- **Pattern**: Subsets (#7)
- **Data Structure**: Array
- **Algorithm**: Backtracking, DFS
- **Tags**: Backtracking, DFS, Subsets


## ☀️ Solution Code

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  # Store all subsets

        def backtrack(start, path):
            res.append(path[:])  # Add a copy of current subset

            for i in range(start, len(nums)):
                path.append(nums[i])      # Choose
                backtrack(i + 1, path)    # Explore
                path.pop()                # Un-choose (Backtrack)

        backtrack(0, [])
        return res
```


## ☀️ Trace

```
input = [[1, 2, 3]]
output = [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]


Start: path=[], start=0
→ res = [[]] → ✅ add to res

i=0 → pick 1 → path=[1]
  → res = [[], [1]] → ✅ add to res

  i=1 → pick 2 → path=[1,2]
    → res = [[], [1], [1,2]] → ✅ add to res

    i=2 → pick 3 → path=[1,2,3]
      → res = [[], [1], [1,2], [1,2,3]] → ✅ add to res
    ← pop 3 → path=[1,2]
  ← pop 2 → path=[1]

  i=2 → pick 3 → path=[1,3]
    → res = [[], [1], [1,2], [1,2,3], [1,3]] → ✅ add to res
  ← pop 3 → path=[1]
← pop 1 → path=[]

i=1 → pick 2 → path=[2]
  → res += [2], [2,3] → ✅ add to res
←

i=2 → pick 3 → path=[3]
  → res += [3] → ✅ add to res


...
```


## ☀️ Line-by-line Script

- I’m defining the subsets function, which takes a list of integers and returns all possible subsets.
- I initialize an empty list res to store the resulting subsets.
- I define a helper function backtrack that takes the current index start and the current path.
- At each recursive call, I append a copy of the current path to the result list.
- I loop from the current index to the end of the array.
- For each index, I append the number to the path, call backtrack recursively with i + 1, and then backtrack by popping that number.
- Finally, after all recursion completes, I return res containing all subsets.
