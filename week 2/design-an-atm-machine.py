class ATM:

    def __init__(self):
        self.notes = defaultdict(int)
        self.order = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.notes[self.order[i]] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        no_of_banknotes = 0
        withdrawn = []
        
        for idx in range(len(self.order) - 1 , -1 , -1):
            count = int(amount // self.order[idx])
           
            if self.notes[self.order[idx]] > 0:
                if count <= self.notes[self.order[idx]]:
                    amount -= (count * self.order[idx])
                    withdrawn.append(count)
                else:
                    amount -= (self.notes[self.order[idx]] * self.order[idx])
                    withdrawn.append(self.notes[self.order[idx]]) 
            else:
                withdrawn.append(0)
            
        if amount != 0:
            return [-1]
        
        withdrawn = withdrawn[::-1]
        for i in range(len(withdrawn)):
            self.notes[self.order[i]] -= withdrawn[i]

        return withdrawn

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)