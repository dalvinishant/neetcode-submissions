class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == len(board) - 1 or j == len(board[0]) - 1 or  i == 0 or j == 0:
                    continue
                if board[i][j] == 'O':
                    # board[i][j] = 'X'
                    if self.checkIfCanBeReplaced(set(), i, j, board):
                        board[i][j] = 'X'
                
    def checkIfCanBeReplaced(self, v, i, j, board):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False

        if (i, j) in v:
            return True
        
        if board[i][j] == 'X':
            return True

        v.add((i,j))

        t = self.checkIfCanBeReplaced(v, i-1, j, board)
        b = self.checkIfCanBeReplaced(v, i+1, j, board)
        l = self.checkIfCanBeReplaced(v, i, j-1, board)
        r = self.checkIfCanBeReplaced(v, i, j+1, board)

        return t and b and l and r