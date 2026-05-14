class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasSet = {}

        for i, n in enumerate(nums):
            c = target - n
            if c not in hasSet:
                hasSet[n] = i
            else:
                return [hasSet[c], i]

            
