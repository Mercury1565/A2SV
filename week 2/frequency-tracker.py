class FrequencyTracker:

    def __init__(self):
        self.tracker = defaultdict(int)
        self.frequency = defaultdict(int)        

    def add(self, number: int) -> None:
        self.frequency[self.tracker[number]] -= 1
        self.tracker[number]+=1
        self.frequency[self.tracker[number]] += 1


    def deleteOne(self, number: int) -> None:
        if self.tracker[number]!=0:
            self.frequency[self.tracker[number]] -= 1
            self.tracker[number]-=1
            self.frequency[self.tracker[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency[frequency]

        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)