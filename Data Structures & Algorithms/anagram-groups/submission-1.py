class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagrams = {}

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            if tuple(count) not in anagrams:
                anagrams[tuple(count)] = [s]
            else:
                anagrams[tuple(count)].append(s)
        
        for a in anagrams.values():
            res.append(a)

        print(res)
        return res


        
                 

