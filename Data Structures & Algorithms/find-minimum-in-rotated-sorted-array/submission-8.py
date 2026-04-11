class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        smallest = nums[left]

        while left <= right:

            mid = (left + right) // 2
            smallest = min(smallest, nums[mid])

            if nums[mid] < nums[right]:
                right = mid-1
            else:
                left = mid+1
        
        return smallest
            
