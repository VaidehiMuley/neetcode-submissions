class Solution:
    def isValid(self, s: str) -> bool:
        lookup_map = {'}':'{', ')':'(', ']':'['}
        stack = []
        for i in s:
            if i in lookup_map:
                if stack and stack[-1] == lookup_map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if len(stack) == 0 else False
            



        
            



        