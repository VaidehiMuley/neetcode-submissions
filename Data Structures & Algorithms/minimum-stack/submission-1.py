class MinStack:

    def __init__(self):
        self.stash = []
        self.min_stash = []

    def push(self, val: int) -> None:
        self.stash.append(val)
        val = min(val, self.min_stash[-1] if self.min_stash else val)
        self.min_stash.append(val)

    def pop(self) -> None:
        self.stash.pop()
        self.min_stash.pop()

    def top(self) -> int:
        return self.stash[-1]

    def getMin(self) -> int:
        return self.min_stash[-1]


