class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start, combo, curr_target):
            if curr_target == 0:
                res.append(combo.copy())
                return
            
            for i in range(start, len(nums)):
                curr = nums[i]
                if curr > curr_target:
                    return
                combo.append(curr)
                backtrack(i, combo, curr_target - curr)
                combo.pop()
            return
        backtrack(0, [], target)
        return res