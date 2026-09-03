class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean the string, remove all special characters and spaces, and lowercase
        # l ptr at beginning and r ptr at the end
        # compare l and r, return False if not equal

        cleanedS = re.sub(r'[^A-Za-z0-9]', '', s).lower()

        l, r = 0, len(cleanedS) - 1

        while l < r:
            if cleanedS[l] != cleanedS[r]:
                return False
            l += 1
            r -= 1

        return True