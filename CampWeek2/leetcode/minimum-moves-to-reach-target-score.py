class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        floor = []
        temp = target

        while temp // 2 and maxDoubles:
            temp //= 2
            floor.append(temp)
            maxDoubles -= 1
        
        if not floor:
            return target - 1
        floor.sort()

        steps = 0
        num = 1
        
        for checkPoints in floor:
            steps += (checkPoints - num)
            steps += 1
            num = checkPoints * 2

        return steps + target - num
            

            
        