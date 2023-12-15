class Bitset:

    def __init__(self, size: int):
        self.zeros = defaultdict(int)
        for i in range(size):
            self.zeros[i] = 1

        self.ones = defaultdict(int)
        self.size = size
      
    def fix(self, idx: int) -> None:
        if idx in self.zeros:
            self.zeros.pop(idx)
            self.ones[idx] += 1

    def unfix(self, idx: int) -> None:
        if idx in self.ones:
            self.ones.pop(idx)
            self.zeros[idx] += 1 

    def flip(self) -> None:
        self.ones , self.zeros = self.zeros , self.ones

    def all(self) -> bool:
        return not bool(self.zeros)

    def one(self) -> bool:
        return bool(self.ones)
       
    def count(self) -> int:
        return len(self.ones)

    def toString(self) -> str:
        answer = [''] * self.size

        for idx in self.zeros:
                answer[idx] = '0'
    
        for idx in self.ones:
                answer[idx] = '1'
         
        return ''.join(answer)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()