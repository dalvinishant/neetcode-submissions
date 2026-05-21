class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1:
            return triplets[0] == target

        triplets_possible = [[False, False] for _ in range(len(target))]

        for i, j, k in triplets:
            if i <= target[0]:
                if i < target[0] and not triplets_possible[0][0]:
                    triplets_possible[0][0] = True
                elif i == target[0] and not triplets_possible[0][1]:
                    triplets_possible[0][1] = True
                    
            if j <= target[1] and i <= target[0]:
                if j < target[1] and not triplets_possible[1][0]:
                    triplets_possible[1][0] = True
                elif j == target[1] and not triplets_possible[1][1]:
                    triplets_possible[1][1] = True

            if k <= target[2] and j <= target[1]:
                if k < target[2] and not triplets_possible[2][0]:
                    triplets_possible[2][0] = True
                elif k == target[2] and not triplets_possible[2][1]:
                    triplets_possible[2][1] = True

        for lower, equal in triplets_possible:
            if not (lower and equal):
                return False
        
        return True