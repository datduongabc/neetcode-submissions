class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_value = float('inf')

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0 or val < self.min_value:
            self.min_value = val

        self.min_stack.append(self.min_value)
        self.stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        if len(self.min_stack) > 0:
            self.min_value = self.min_stack[-1]
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]