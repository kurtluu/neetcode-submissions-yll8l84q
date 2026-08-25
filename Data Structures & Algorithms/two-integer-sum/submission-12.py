class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        cDict = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in cDict:
                return [cDict[complement], i]
            
            cDict[nums[i]] = i

        return -1