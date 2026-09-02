class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {'}':'{', ']':'[', ')':'('}
        stack = []

        for p in s:
            if p in pMap:
                if stack and stack[-1] == pMap[p]:
                    stack.pop()
                else:
                    # once a mismatch i seen, return False, nothing can solve ex '([})'. Once we get to 3rd char it'll be broken forever
                    return False
            else:
                stack.append(p)    
        
        return not stack
            
