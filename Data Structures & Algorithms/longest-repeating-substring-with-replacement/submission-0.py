class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        res = 0
        maxFreq = 0

        l = 0
        for r, ch in enumerate(s):
            count[ord(ch) - ord('A')] += 1
            maxFreq = max(maxFreq, count[ord(ch) - ord('A')])

            while(r - l + 1) - maxFreq > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
            
