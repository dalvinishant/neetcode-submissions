
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLast = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        
        node.isLast = True

    def search(self, word: str, node = None) -> bool:
        print(word)
        node = self.root if not node else node
        for i, letter in enumerate(word):
            if letter == '.':
                for j in node.children:
                    if self.search(word[i+1:], node = node.children[j]):
                        return True
                return False
            elif letter not in node.children:
                return False
            node = node.children[letter]
        
        return node.isLast