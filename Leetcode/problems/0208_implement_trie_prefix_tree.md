# Leetcode 0208 - Implement Trie (Prefix Tree)

## ☀️ UMPIRE
- **Understand**: Implement a Trie (Prefix Tree) with three methods: `insert(word)`, `search(word)`, and `startsWith(prefix)`
- **Match**: This is a prefix-based problem involving repeated character lookups — suitable for Trie (tree-based structure)
- **Plan**: Use a TrieNode class with a dictionary `children` and an `isEnd` flag; Traverse or create nodes during insert, and check structure during search and prefix lookup
- **Implement**: See below
- **Review**: Ensure that new TrieNodes are created only when needed and that `isEnd` correctly marks word boundaries
- **Evaluate**: Time O(n) per operation where n = word length; Space O(n * m) where m = number of inserted words

## ☀️ Metadata
- **Appears In**: Grind75
- **Pattern**: Trie / Prefix Tree
- **Data Structure**: Tree, HashMap (dict)
- **Algorithm**: Iterative character traversal
- **Tags**: Trie, Prefix, String, Tree

## ☀️ Solution Code

```python
class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes: key = character, value = TrieNode
        self.children = {}
        # Flag to mark the end of a complete word
        self.isEnd = False


class Trie:
    def __init__(self):
        # Initialize the root of the Trie (empty node)
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
```

## ☀️ Trace

```
insert("apple")
→ create child 'a' → create child 'p' → create child 'p' → create child 'l' → create child 'e'
→ mark 'e'.isEnd = True

search("apple")
→ check 'a' → check 'p' → check 'p' → check 'l' → check 'e'
→ at 'e', isEnd = True → return True

search("app")
→ check 'a' → check 'p' → check 'p'
→ at second 'p', isEnd = False → return False

startsWith("app")
→ check 'a' → check 'p' → check 'p'
→ all characters exist → return True
```

## ☀️ Line-by-line Typing Script

- I’m defining a `TrieNode` class that contains a dictionary for children and a boolean flag `isEnd`.
- The `Trie` class contains a root node which is just a `TrieNode` instance.
- In `insert(word)`, I start from the root node and loop through each character in the word.
- If the character is not in the current node’s children, I create a new `TrieNode()` and store it in `children[ch]`.
- Then I move to the child node corresponding to that character.
- After processing all characters, I mark the final node with `isEnd = True` to signify the end of a valid word.
- In `search(word)`, I again start from the root and follow each character.
- If any character is missing in the children, I return False immediately.
- If I reach the end, I check if the current node’s `isEnd` is True — only then return True.
- In `startsWith(prefix)`, I follow the same logic as `search`, but don’t care about `isEnd` — just that all characters exist.
- These methods allow fast insertion and lookup of words and prefixes using the Trie structure.
