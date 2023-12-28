class Robot:

    def __init__(self, width: int, height: int):
        self.ends = (width - 1 , height - 1)
        self.position = [0,0]
        self.flag = True
        

    def step(self, num: int) -> None:
        perimeter = 2*(self.ends[0] + self.ends[1])
        num = num % perimeter
        self.flag = False
    
        while num > 0:
            if self.position[1] == 0:#East
                if self.position[0] + num > self.ends[0]:
                    temp = self.ends[0] - self.position[0]
                    num -= temp
                    self.position[0] = self.ends[0]
                else:
                    self.position[0] += num
                    num = 0

            if self.position[0] == self.ends[0]:#North
                if self.position[1] + num > self.ends[1]:
                    temp = self.ends[1] - self.position[1]
                    num -= temp
                    self.position[1] = self.ends[1]
                else:
                    self.position[1] += num
                    num = 0

            if self.position[1] == self.ends[1]:#West
                if self.position[0] - num < 0:
                    temp = self.position[0]
                    num -= temp
                    self.position[0] = 0
                else:
                    self.position[0] -= num
                    num = 0
            
            if self.position[0] == 0:#South
                if self.position[1] - num < 0:
                    temp = self.position[1]
                    num -= temp
                    self.position[1] = 0
                else:
                    self.position[1] -= num
                    num = 0
            
            

    def getPos(self) -> List[int]:
        return self.position

    def getDir(self) -> str:
        if self.position[0] == 0 and self.position[1] == 0:
            if self.flag:
                return 'East'
            return 'South'

        if self.position[1] == 0:
            return 'East'
        elif self.position[0] == self.ends[0]:
            return 'North'
        elif self.position[1] == self.ends[1]:
            return 'West'
        elif self.position[0] == 0:
            return 'South'
        
    
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()