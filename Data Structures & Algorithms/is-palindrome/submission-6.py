class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedS = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        l, r = 0, len(cleanedS) - 1

        while l < r:
            if cleanedS[l] != cleanedS[r]:
                return False
            l += 1
            r -= 1

        return True
        


