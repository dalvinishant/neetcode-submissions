class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        exists = False
        for i in range(0, len(matrix)):
            if target <= matrix[i][-1]:
                if target == matrix[i][-1]:
                    exists = True
                    break
                for j in range(0, len(matrix[i])):
                    if target == matrix[i][j]:
                        exists = True
                        break
        return exists

    

