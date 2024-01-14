class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l , r = 0 , 1
        result = inf
        lastOcc = {}

        for i in range(len(cards)):
            if cards[i] not in lastOcc:
                lastOcc[cards[i]] = [i]
                continue
            lastOcc[cards[i]].append(i)

        for k in lastOcc:
            if len(lastOcc[k]) == 1:
                continue
            while len(lastOcc[k]) > 1:
                x = lastOcc[k].pop() - lastOcc[k][-1] + 1
                result = min(result , x)

        return -1 if result == inf else result
       