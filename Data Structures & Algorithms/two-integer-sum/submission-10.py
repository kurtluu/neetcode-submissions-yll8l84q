class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cDict = {}

        for i, n in enumerate(nums):
            c = target - n
            if c not in cDict:
                cDict[n] = i
            else:
                return [cDict[c], i]
        
        return -1