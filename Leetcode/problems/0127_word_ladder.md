# Leetcode 0127 - Word Ladder

## ☀️ UMPIRE

- **Understand**: Given a start word, an end word, and a word list, return the length of the shortest transformation sequence from start to end, changing one letter at a time, where each intermediate word must exist in the word list.
- **Match**: Graph search problem; input is word list, goal is shortest path with single-letter transformations.
- **Plan**: Use BFS to explore all word transformations level by level, marking visited words to prevent cycles.
- **Implement**: See below
- **Review**: Check one-letter transformation logic and visited handling
- **Evaluate**: Time O(N \* 26 \* L), where N is the number of words, L is word length; Space O(N) for queue and visited set

---

## ☀️ Metadata

- **Appears In**: Grind75
- **Pattern**: BFS (#2)
- **Data Structure**: Set, Queue
- **Algorithm**: Breadth-First Search
- **Tags**: BFS, Graph, Shortest Path, String

---

## ☀️ Solution Code

```python
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordSet = set(wordList)  # Use a set for O(1) lookups
        if endWord not in wordSet:
            return 0

        queue = deque()
        queue.append((beginWord, 1))      # Start from the beginWord with step count 1
        visited = set([beginWord])        # Track visited words to avoid revisiting

        while queue:
            word, steps = queue.popleft()

            # Try replacing each character in the word with 'a' to 'z'
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = word[:i] + c + word[i+1:]

                    if nextWord == endWord:
                        return steps + 1

                    # Only consider unvisited and valid words
                    if nextWord in wordSet and nextWord not in visited:
                        queue.append((nextWord, steps + 1))  # Enqueue for BFS
                        visited.add(nextWord)                # Add to visited set (must be hashable)

        return 0  # If no transformation path is found
```

---

## ☀️ Trace

```
queue = [('hit', 1)]
visited = {'hit'}

→ pop ('hit', 1)
   → generate: 'hot' in wordSet → append ('hot', 2), add to visited
queue = [('hot', 2)]
visited = {'hit', 'hot'}

→ pop ('hot', 2)
   → generate: 'dot', 'lot' → both in wordSet → append ('dot', 3), ('lot', 3)
queue = [('dot', 3), ('lot', 3)]
visited = {'hit', 'hot', 'dot', 'lot'}

→ pop ('dot', 3)
   → generate: 'dog' → append ('dog', 4)
queue = [('lot', 3), ('dog', 4)]
visited = {..., 'dog'}

→ pop ('dog', 4)
   → generate: 'cog' → match found → return 5
```

---

## ☀️ Line-by-line Typing Script

- Define the function `ladderLength` inside a `Solution` class.
- Convert `wordList` to a set for fast lookup.
- If the `endWord` isn’t in the set, we can return 0 early.
- Initialize a queue and begin with the `beginWord` and step count 1.
- Create a `visited` set to track words we’ve already used.
- While the queue is not empty, pop the leftmost item: current word and current step count.
- For each index in the word, try replacing the character with all letters from 'a' to 'z'.
- If the resulting word equals `endWord`, return current step + 1.
- If the word is valid and not yet visited, enqueue it and mark it visited.
- If we exit the loop with no result, return 0.
