class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sNums = sorted(nums)
        res = []
        
        for i, n in enumerate(sNums):
            if n > 0:
                break

            if i > 0 and n == sNums[i - 1]:
                continue

            l, r = i + 1, len(sNums) - 1
            while (l < r):
                currSum = n + sNums[l] + sNums[r]
                if currSum < 0:
                    l += 1 
                elif currSum > 0:
                    r -= 1
                else: # currSum == 0 
                    res.append([n, sNums[l], sNums[r]])
                    l += 1
                    r -= 1
                    while sNums[l] == sNums[l - 1] and l < r:
                        l += 1
        return res


            
                    