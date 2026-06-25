class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        aMap = {}

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            
            if tuple(count) not in aMap:
                aMap[tuple(count)] = []
            aMap[tuple(count)].append(word)
            
        for value in aMap.values():
            res.append(value)

        return res
                
        
                