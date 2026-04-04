class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val = set()
        for n in nums:
            if n in val:
                return True
            val.add(n)
        return False