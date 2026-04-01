class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        self.generate(sets, [], nums)
        return sets
        
    def generate(self, s, v, nums):
        s.append(v.copy())
        if len(nums) == 0:
            return 
        for i, num in enumerate(nums): 
            v.append(num)
            self.generate(s, v, nums[i+1:])
            v.pop(-1)
        return