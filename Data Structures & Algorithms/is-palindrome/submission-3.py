class Solution:
    def isPalindrome(self, s: str) -> bool:
        cS = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        l, r = 0, len(cS) - 1

        while l <= r:
            if cS[l] == cS[r]:
                l += 1 
                r -= 1
            else:
                return False
        return True
