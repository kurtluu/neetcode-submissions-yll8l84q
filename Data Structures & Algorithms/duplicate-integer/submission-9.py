class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasSet = set()

        for n in nums:
            if n not in hasSet:
                hasSet.add(n)
            else:
                return True
        
        return False
            