from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordSet = set(wordList)  # Use a set for O(1) lookups
        if endWord not in wordSet:
            return 0

        queue = deque()
        queue.append((beginWord, 1)) # Start from the beginWord with step count 1
        visited = set([beginWord])   # Track visited words to avoid revisiting

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
                        visited.add(nextWord) # Add to visited set (must be hashable)

        return 0  # If no transformation path is found
