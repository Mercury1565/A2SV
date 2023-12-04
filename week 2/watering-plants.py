class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cap = capacity
        steps = 0

        for i in range(len(plants)):
            if plants[i] <= cap:
                cap -= plants[i]
                steps += 1
                continue
            
            cap = capacity - plants[i]
       
            steps += i * 2
            steps += 1

        return steps
            
        