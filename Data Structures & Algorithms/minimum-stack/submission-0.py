class MinStack:

    def __init__(self):
        self.stack = list()
        self.least = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.least) > 0:
            self.least.append(min(self.least[-1],val))
        else:
            self.least.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.least.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.least[-1]

        
