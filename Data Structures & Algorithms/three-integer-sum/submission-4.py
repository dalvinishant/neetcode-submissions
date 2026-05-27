from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        i = 0 
        j = 1
        k = len(nums) - 1
        target = 0
        res = set()
        while i < k:
            while j < k:
                n =  nums[i] + nums[j] + nums[k]
                # print(n , target, nums[i], nums[j], nums[k])
                if n == target:
                    res.add((nums[i], nums[j], nums[k]))
                    j+=1
                    # break
                elif n > target:
                    k -= 1
                else:
                    j+=1
            i += 1
            j = i+1
            k = len(nums) - 1
        return list(res)

