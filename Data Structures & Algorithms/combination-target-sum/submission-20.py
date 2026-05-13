class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(start, combo, curr_target):
            if curr_target == 0:
                res.append(combo[:])
                return

            for i in range(start, len(nums)):
                if nums[i] > curr_target:
                    return
                
                combo.append(nums[i])
                dfs(i, combo, curr_target - nums[i])
                combo.pop()
            return
        
        dfs(0, [], target)
        return res
            