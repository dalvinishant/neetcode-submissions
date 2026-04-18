class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return self.partitionable(0, nums, {})
    
    def partitionable(self, curr_sum, nums, mem):

        if not nums:
            print('returning')
            return False

        print(curr_sum, sum(nums), nums)
        if curr_sum == sum(nums):
            return True
        
        if curr_sum in mem:
            return mem[curr_sum]

        for i, n in enumerate(nums):
            new_sum = curr_sum + n
            exists = self.partitionable(new_sum, nums[:i]+nums[i+1:], mem)
            print('exists')
            if exists:
                mem[curr_sum] = True
                return True
        print('returning')
        mem[curr_sum] = False
        return False

