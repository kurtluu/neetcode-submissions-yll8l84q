class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hasSet = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in hasSet:
                hasSet.remove(s[l])
                l += 1
            hasSet.add(s[r])
            res = max(res, r - l + 1)
        return res
            

        
            
            
