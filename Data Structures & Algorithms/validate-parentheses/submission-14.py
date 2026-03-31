
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        #edge case
        if (len(s) % 2) == 1:
            return False

        for p in s:
            if p == "(" or p == "{" or p == "[":
                stack.append(p)
            elif p == ")":
                if not stack: 
                    return False
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif p == "}":
                if not stack:
                    return False
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif p == "]":
                if not stack:
                    return False
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False           
            print(stack)

        print(stack)
        if stack: 
            return False
        else:
            return True

        
                    

        

        