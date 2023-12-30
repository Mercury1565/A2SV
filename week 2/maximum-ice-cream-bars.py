class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ssum = 0
        costs.sort()

        for i in range(len(costs)):
            ssum += costs[i]
            if ssum == coins:
                return i + 1
            elif ssum > coins:
                return i
        return len(costs)
        