class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        for i in range(len(nums) - 2):
            l, r = i + 1, i + 2
            while (l < len(nums) - 1):
                #print([nums[i], nums[l], nums[r]])
                if nums[i] + nums[l] + nums[r] == 0:
                    res.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                if r < len(nums) - 1:
                    r += 1
                else:
                    l += 1
                    r = l + 1 

        return [list(t) for t in res]