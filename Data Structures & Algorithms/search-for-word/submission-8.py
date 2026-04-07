class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.search(i, j, '', word, board, set()):
                        return True
        return False
    
    def search(self, i, j, s, word, board, v):
        if s == word:
            return 1

        if i < 0 or i>=len(board) or j <0 or j>=len(board[0]):
            return 0
        
        
        if (i, j) in v:
            return 0
            
        
        if len(s) > len(word) or s != word[:len(s)]:
            return 0

        new_s = s + board[i][j]
        v.add((i,j))
            
        top = self.search(i-1, j, new_s, word, board, v)
        bottom = self.search(i+1, j, new_s, word, board, v)
        left = self.search(i, j-1, new_s, word, board, v)
        right= self.search(i, j+1, new_s, word, board, v)
        
        v.remove((i, j))
        return  max(bottom, right, top, left)
        