class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aDict = {}

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord('a') - ord(ch)] += 1

            if tuple(count) not in aDict:
                aDict[tuple(count)] = [s]
            else:
                aDict[tuple(count)].append(s)

        return list(aDict.values())