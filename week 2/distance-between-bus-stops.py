class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)

        x = min(start , destination)
        y = max(start , destination)
        
        distance_1 = sum(distance[x : y])
        distance_2 = total - distance_1

        return min(distance_1 , distance_2)
        
        