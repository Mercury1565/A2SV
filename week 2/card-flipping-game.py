class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        min_card = inf
        not_allowed = set()

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                not_allowed.add(fronts[i])
    
        for i in range(len(fronts)):
            if backs[i] not in fronts:
                min_card = min(min_card , backs[i])

            if fronts[i] not in not_allowed:
                min_card = min(min_card , fronts[i])

        return 0 if min_card == inf else min_card
        