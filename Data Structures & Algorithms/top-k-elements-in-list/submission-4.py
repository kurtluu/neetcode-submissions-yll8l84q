class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a hashmap with the number and the count
        # add to res, k times
        
        # elements dictionary { element : count }
        eDict = {} 
        res = []

        for n in nums:
            if n not in eDict:
                eDict[n] = 1
            else:
                eDict[n] += 1
        
        # find greatest count, add to res 
        # then delete from hashMap
        while k > 0:
            maxFreq = max(eDict, key=eDict.get)
            res.append(maxFreq)
            del eDict[maxFreq]
            k -=1

        return res
            


