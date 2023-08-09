# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    
    def __init__(self, char=""):
        self.char = char
        self.letters = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        node = self.root
        for c in word:
            if c in node.letters.keys():
                node = node.letters[c]
            else:
                newNode = TrieNode(c)
                node.letters[c] = newNode
                node = newNode
        node.isWord = True
        return

    def search(self, word: str) -> bool:
        
        node = self.root
        for c in word:
            if c not in node.letters.keys():
                return False
            node = node.letters[c]

        return node.isWord
        

    def startsWith(self, prefix: str) -> bool:

        node = self.root
        for c in prefix:
            if c not in node.letters.keys():
                return False
            node = node.letters[c]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)