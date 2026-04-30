class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] 
        res = []
        open_count = close_count = 0
        def recursive(open_count, close_count):            
            ## result condition
            if open_count == close_count == n:
                res.append("".join(stack))
                return res

            if open_count < n:
                stack.append("(")
                recursive(open_count+1 , close_count)
                stack.pop()


            if close_count < open_count:
                stack.append(")")
                recursive(open_count , close_count+1)
                stack.pop()

            

        recursive(open_count, close_count)
        return res



        