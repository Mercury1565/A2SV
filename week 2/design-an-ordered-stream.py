class OrderedStream:

    def __init__(self, n: int):
        self.dic = dict()
        self.pointer = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.dic[idKey] = value

        arr = []
        while self.pointer in self.dic:
            arr.append(self.dic[self.pointer])
            self.pointer += 1

        return arr
        
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
