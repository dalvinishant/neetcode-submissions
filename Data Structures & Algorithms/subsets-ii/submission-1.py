class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sets = []
        nums.sort()
        self.genSubsets( sets, [], nums)
        return sets
    
    def genSubsets(self, s, v, nums):
        s.append(v.copy())
        if len(nums) == 0:
            return
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            v.append(nums[i])
            self.genSubsets(s, v, nums[i+1:])
            v.pop(-1)
        