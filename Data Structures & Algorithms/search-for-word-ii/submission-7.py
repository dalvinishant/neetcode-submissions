class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLast = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.createTrie(words)
        # print(self.root.children)
        self.present_words = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search('', i, j, board, set())
        return list(self.present_words)

    def search(self, s, i, j, board, visited):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            # print('returning', i)
            return 
        # print(visited)
        if (i, j) in visited:

            return

        new_s = s+board[i][j]
        present, complete = self.trieSearch(new_s)
        # print(new_s, present, complete)
        if not present:
            return

        if present and complete:
            self.present_words.add(new_s)
        
        visited.add((i, j))
        # print(new_s, i, j, visited)
        r = self.search(new_s, i, j+1, board, visited)
        l = self.search(new_s, i, j-1, board, visited)
        t = self.search(new_s, i-1, j, board, visited)
        b = self.search(new_s, i+1, j, board, visited)
        visited.remove((i,j))

    def trieSearch(self, prefix) -> (bool, bool):
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False, False
            node = node.children[letter]
        
        return True, node.isLast

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
        