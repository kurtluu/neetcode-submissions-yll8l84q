class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for n in nums:
            if n in count: 
                count[n] += 1
            else: 
                count[n] = 1
        
        while (k > 0):
            maxValKey = max(count, key=count.get)
            res.append(maxValKey)
            count.pop(maxValKey)
            k -= 1
        
        return res