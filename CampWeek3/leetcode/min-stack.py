class MinStack:

    def __init__(self):
        self.stack = []
        self.minfreq = defaultdict(int)
        self.minstack = []

    def push(self, val: int) -> None:
        if not self.minstack:
            self.minstack.append(val)
        elif val < self.minstack[-1]:
            self.minstack.append(val)
        
        self.minfreq[self.minstack[-1]] += 1
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

        self.minfreq[self.minstack[-1]] -= 1
        freq = self.minfreq[self.minstack[-1]]
        
        if freq == 0:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()