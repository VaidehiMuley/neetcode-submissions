class MinStack:

    def __init__(self):
        self.stash = []

    def push(self, val: int) -> None:
        self.stash.append(val)

    def pop(self) -> None:
        self.stash.pop()

    def top(self) -> int:
        return self.stash[-1]

    def getMin(self) -> int:
        return min(self.stash)
