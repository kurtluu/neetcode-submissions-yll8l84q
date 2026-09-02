class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {'}':'{', ']':'[', ')':'('}
        stack = []

        for p in s:
            if p in pMap:
                if stack and stack[-1] == pMap[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
            
        return not stack
                
                