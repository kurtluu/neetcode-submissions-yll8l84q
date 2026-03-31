class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedS = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l, r = 0, len(cleanedS) - 1

        while (l < r):
            print(cleanedS[l], cleanedS[r])
            if cleanedS[l] == cleanedS[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True
