class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(start, combo, curr_target):
            if curr_target == 0:
                res.append(combo[:])
                return

            for i in range(start, len(nums)):                
                if i > start and nums[i] == nums[i - 1]:
                    continue

                if nums[i] > curr_target:
                    return
                
                combo.append(nums[i])
                dfs(i + 1, combo, curr_target - nums[i])
                combo.pop()
            return
        
        dfs(0, [], target)
        return res
            