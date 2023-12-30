class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        num_piles = int(len(piles) / 3)
        ssum = 0
        x = -2

        for i in range(num_piles):
            ssum += piles[x]
            x -= 2
        return ssum
        