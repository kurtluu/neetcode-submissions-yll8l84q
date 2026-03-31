class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = [0] * 26 
        countT = [0] * 26

        for ch in s: 
            countS[ord(ch) - ord('a')] += 1
        for ch in t:
            countT[ord(ch) - ord('a')] += 1
        
        if countS == countT: 
            return True
        else:
            return False