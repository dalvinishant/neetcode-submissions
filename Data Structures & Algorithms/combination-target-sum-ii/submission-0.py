class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        comb2 = []
        candidates.sort()
        self.findSum(0, comb2, [], candidates, target)
        return comb2
    
    def findSum(self, i, comb, visited, nums, target):
        if target == 0:
            comb.append(visited.copy())
            return
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j-1]:
                continue
            if target - nums[j] < 0:
                continue
            visited.append(nums[j])
            self.findSum(j+1, comb, visited, nums, target - nums[j])
            visited.pop(-1)
        return