class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        comb = []
        self.findSum(0, comb, [], nums, target)
        return comb

    def findSum(self, cur_i, comb, visited, nums, target):

        if target == 0:
            comb.append(visited.copy())
            return comb
        for i in range(cur_i, len(nums)):
            if target - nums[i] < 0:
                continue 
            visited.append(nums[i])
            # print(cur_i, visited, nums[i], target-nums[i])
            self.findSum(i, comb, visited, nums, target-nums[i])
            visited.pop(-1)
        return comb