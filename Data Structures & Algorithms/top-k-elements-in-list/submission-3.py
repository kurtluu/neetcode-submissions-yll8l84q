class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        numsDic = {}
        
        for n in nums:
            if n not in numsDic:
                numsDic[n] = 1
            else:
                numsDic[n] += 1
        
        while k > 0:
            maxNum = max(numsDic, key=numsDic.get)
            res.append(maxNum)
            del numsDic[maxNum]
            k -= 1

        return res
        
            
