class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLast = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.createTrie(words) # O(w)
        self.present_words = set()
        # O(m*n)
        for i in range(len(board)):
            for j in range(len(board[0])):
                # O(m*n)
                self.search("", i, j, board, set(), self.root)
        return list(self.present_words)

    def search(self, word, i, j, board, visited, node):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] not in node.children:
            return 

        if (i, j) in visited:
            return
        
        visited.add((i, j))
        node = node.children[board[i][j]]
        word += board[i][j]
        if node.isLast:
            self.present_words.add(word)
        r = self.search(word, i, j+1, board, visited, node)
        l = self.search(word, i, j-1, board, visited, node)
        t = self.search(word, i-1, j, board, visited, node)
        b = self.search(word, i+1, j, board, visited, node)
        visited.remove((i,j))

    def createTrie(self, words):
        node = self.root
        for word in words:
            tmp = node
            for letter in word:
                if letter not in node.children:
                    node.children[letter] = TrieNode()
                node = node.children[letter]
            node.isLast = True
            node = tmp
        