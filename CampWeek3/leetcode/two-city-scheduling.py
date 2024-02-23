class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda a: a[0] - a[1])
        cost = 0
        for i in range(len(costs)):
            if i < len(costs) / 2:
                cost +=  costs[i][0]
            else:
                cost +=  costs[i][1]
        return cost