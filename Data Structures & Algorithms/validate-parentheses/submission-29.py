class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = {'}':'{', ')':'(', ']':'['}

        for ch in s:
            if ch in pMap:
                if stack and stack[-1] == pMap[ch]:
                    stack.pop()
                else:
                    return False
                    # "[( ] )"
            else:
                stack.append(ch)

        # if stack empty, compared every s and is valid
        return not stack