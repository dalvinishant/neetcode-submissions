class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        # Rows
        for i in range(9):
            seen_row = set()
            for j in range(9):

                if board[i][j] == '.':
                    continue
                if board[i][j] in seen_row:
                    return False
                seen_row.add(board[i][j])
        
        # Cols
        for i in range(9):
            seen_col = set()
            for j in range(9):

                # Cols
                if board[j][i] == '.':
                    continue
                if board[j][i] in seen_col:
                    return False
                seen_col.add(board[j][i])
        
        for sq in range(9):
            seen_square = set()
            for i in range(3):
                for j in range(3):
                    row = (sq//3) * 3 + i
                    col = (sq%3) * 3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen_square:
                        return False
                    seen_square.add(board[row][col])

        return True