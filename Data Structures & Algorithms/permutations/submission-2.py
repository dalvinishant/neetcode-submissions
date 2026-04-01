class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.generate(permutations, [], set(), nums)
        return permutations
    
    def generate(self, permutations, visited, visit_set, nums):
        if len(visited) == len(nums):
            permutations.append(visited.copy())
            return permutations
        for num in nums: 
            if num in visit_set:
                continue
            visited.append(num)
            visit_set.add(num)
            self.generate(permutations, visited, visit_set, nums)
            visited.pop(-1)
            visit_set.remove(num)