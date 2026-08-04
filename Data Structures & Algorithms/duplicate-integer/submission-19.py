class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasSet = set()

        for n in nums:
            if n in hasSet:
                return True
            hasSet.add(n)
        return False