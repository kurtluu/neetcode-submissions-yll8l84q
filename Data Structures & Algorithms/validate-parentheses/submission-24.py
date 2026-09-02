class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {'}':'{', ']':'[', ')':'('}
        stack = []

        for ch in s:
            if ch in pMap:
                if stack and stack[-1] == pMap[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return not stack
                