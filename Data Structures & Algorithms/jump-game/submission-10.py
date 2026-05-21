class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i = 0
        n = len(nums)
        c = 0
        while i < n-1:
            if nums[i] == 0:
                return False
            tmp = [(i+1+j+x, i+1+j) for j, x in enumerate(nums[i + 1 : i + 1 + nums[i]])]
            heapq.heapify(tmp)
            i = heapq.nlargest(1, tmp)[0][1]
            
            

        return True