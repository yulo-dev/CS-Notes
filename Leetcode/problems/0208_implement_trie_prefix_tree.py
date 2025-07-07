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


# Test the Trie — your own test area
def main():
    trie = Trie()

    # Insert words
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")
    trie.insert("bat")

    # Search full words
    print(trie.search("apple"))   # True
    print(trie.search("app"))     # True
    print(trie.search("appl"))    # False
    print(trie.search("banana"))  # True
    print(trie.search("bananas")) # False

    # Test prefixes
    print(trie.startsWith("app"))    # True
    print(trie.startsWith("ban"))    # True
    print(trie.startsWith("bat"))    # True
    print(trie.startsWith("bad"))    # False
    print(trie.startsWith("cat"))    # False


# Run your test function
main()
