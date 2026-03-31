class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDict = set()

        for i in nums:
            if i in hasDict:
                return True
            else:
                hasDict.add(i)
        return False