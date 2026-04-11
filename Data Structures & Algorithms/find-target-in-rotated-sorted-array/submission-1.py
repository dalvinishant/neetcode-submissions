class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left

        if (res := self.binarySearch(0, pivot - 1, target, nums)) != -1:
            return res
        else:
            return self.binarySearch(pivot, len(nums) - 1, target, nums)
        
    
    def binarySearch(self, left, right, target, nums):
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                left = mid+1
            else:
                right = mid-1
        
        return -1
            