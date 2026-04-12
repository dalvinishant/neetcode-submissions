class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_val:
            self.min_val = [val]
        else:
            self.min_val += [min(val, self.min_val[-1])]
        # print('push', self.stack, self.min_val)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.min_val.pop(-1)
        # print('pop ', self.stack, self.min_val)

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # print('getMin ',self.stack, self.min_val)
        return self.min_val[-1]
