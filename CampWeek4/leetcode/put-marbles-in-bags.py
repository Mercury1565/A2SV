class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights) <= 2 or len(weights) == k:
            return 0

        div = []
        for i in range(len(weights) - 1):
            div.append(weights[i] + weights[i + 1])

        div.sort()

        maximal_score = 0
        minimal_score = 0

        for j in range(k - 1):
            maximal_score += div[-1 * (j + 1)]
            minimal_score += div[j]

        return maximal_score - minimal_score