class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i, j = 0, 0
        while i < len(nums1) or j < len(nums2):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    nums.append(nums1[i])
                    i += 1
                else:
                    nums.append(nums2[j])
                    j += 1
            if i >= len(nums1) and j < len(nums2):
                nums.append(nums2[j])
                j += 1
            if j >= len(nums2) and i < len(nums1):
                nums.append(nums1[i])
                i += 1
            
        print(nums)

        if len(nums) % 2 == 0:
            med_l, med_r = len(nums)//2 - 1, len(nums)//2
            return (nums[med_l] + nums[med_r])/2
        else:
            return nums[len(nums)//2]

                

