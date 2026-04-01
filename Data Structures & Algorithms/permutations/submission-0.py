class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.generate(permutations, [], nums)
        return permutations
    
    def generate(self, permutations, visited, nums):
        if len(visited) == len(nums):
            permutations.append(visited.copy())
            return permutations
        for num in nums: 
            if num in visited:
                continue
            visited.append(num)
            self.generate(permutations, visited, nums)
            visited.pop(-1)