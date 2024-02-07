class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Once again good old prefix sum

        n = max(trips , key = lambda a : a[2])[2]
        passenger = [0] * n

        for trip in trips:
            passenger[trip[1]] += trip[0]
            if trip[2] < n:
                passenger[trip[2]] -= trip[0]

        for i in range(1 , n):
            passenger[i] += passenger[i - 1]
    
        return max(passenger) <= capacity

            
