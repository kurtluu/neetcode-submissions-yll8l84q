class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasN = {};

        for i, n in enumerate(nums):
            comp = target - n

            if comp in hasN:
                return [hasN[comp], i]
            
            hasN[n] = i