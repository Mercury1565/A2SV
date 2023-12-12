class UndergroundSystem:

    def __init__(self):
        self.customerCheckIn = defaultdict(tuple)
        self.finished = defaultdict(list)
  
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customerCheckIn[id] = (stationName , t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        tstart = self.customerCheckIn[id][1]
        start = self.customerCheckIn[id][0]

        self.finished[(start , stationName)].append(t - tstart)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        arr = self.finished[(startStation , endStation)]
        
        return sum(arr) / len(arr)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)