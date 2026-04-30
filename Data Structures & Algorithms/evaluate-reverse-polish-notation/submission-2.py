class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stash = []
        for i in tokens:
            if i in {"+", "-", "*", "/"}:
                right = int(stash.pop())
                left = int(stash.pop())
                if i == '+':
                    stash.append(left + right)
                elif i == '-':
                    stash.append(left - right)
                elif i == '*':
                    stash.append(left * right)
                elif i == '/':
                    stash.append(int(left / right))  # truncate toward zero
            else:
                stash.append(int(i))
        return stash[-1]