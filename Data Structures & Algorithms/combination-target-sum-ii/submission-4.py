class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, combo, curr_target):
            if curr_target == 0:
                res.append(combo[:])
                return
            
            for i in range(start,  len(candidates)):
                curr = candidates[i]

                if i > start and candidates[i] == candidates[i - 1]:
                    continue                    

                if curr > curr_target:
                    return

                combo.append(curr)
                backtrack(i + 1, combo, curr_target - curr)
                combo.pop()
            return
        
        backtrack(0, [], target)
        return res