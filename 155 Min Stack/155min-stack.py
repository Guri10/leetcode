class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            # self.minStack.pop()
            # print(self.minStack)
            self.minStack.append(val)
        # elif self.minStack:
        #     self.minStack.pop()
        #     self.minStack.append(val)
        
        print(self.minStack)
        # print(self.stack)
        print('-------------')
    def pop(self) -> None:
        if self.stack:
            a = self.stack[-1]
            # print(a) 
            # print(self.stack.pop())
            # print(self.stack)
            self.stack.pop()
            # print(self.stack)
            # print(self.minStack[-1])
            if self.minStack and a == self.minStack[-1]:
                self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()