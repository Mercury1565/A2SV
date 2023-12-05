class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        gotta_ya = inf

        for ghost in ghosts:
            gotta_ya = min(abs(target[0] - ghost[0]) + abs(target[1] - ghost[1]) , gotta_ya)

        return abs(target[0]) + abs(target[1]) < gotta_ya
        