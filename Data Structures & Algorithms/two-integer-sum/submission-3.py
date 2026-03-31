class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasN = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hasN:
                return [hasN[comp], i]
            hasN[nums[i]] = i

        return []