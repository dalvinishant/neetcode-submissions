class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i = 0
        n = len(nums)
        c = 0
        while i < n-1:
            if nums[i] == 0:
                return False
            tmp = [(i+1+j+x, i+1+j) for j, x in enumerate(nums[i + 1 : i + 1 + nums[i]])]
            print(tmp)
            heapq.heapify(tmp)
            print(i+1, i+1 + nums[i], nums, tmp, heapq.nlargest(1, tmp))
            i = heapq.nlargest(1, tmp)[0][1]
            # print(i)
            # c+=1
            # if c == 4:
            #     break
            
            

        return True