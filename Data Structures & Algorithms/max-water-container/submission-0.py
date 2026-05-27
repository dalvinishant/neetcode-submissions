class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        if not heights:
            return 0

        l, r = 0, len(heights) - 1
        max_water = 0
        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            area = h * w
            max_water = max(max_water, area)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_water
