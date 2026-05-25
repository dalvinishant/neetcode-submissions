class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref_prod = [0] * (n)
        suff_prod = [0] * n
        pref_prod[0] = suff_prod[n-1] = 1
        for i in range(1, n):
            pref_prod[i] = nums[i - 1] * pref_prod[i-1]
        
        for j in range(n-2, -1, -1):
            suff_prod[j] = nums[j + 1] * suff_prod[j+1]
        
        for k in range(n):
            res[k] = pref_prod[k] * suff_prod[k]
        
        return res