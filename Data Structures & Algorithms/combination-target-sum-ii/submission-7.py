class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(start, combo, curr_target):
            if curr_target == 0:
                res.append(combo[:])
                return
            
            for i in range(start, len(nums)):
                curr = nums[i]

                if i > start and nums[i] == nums[i - 1]:
                    continue

                if curr > curr_target:
                    return

                combo.append(curr)
                dfs(i + 1, combo, curr_target - curr)
                combo.pop()

            return
        
        dfs(0, [], target)
        return res