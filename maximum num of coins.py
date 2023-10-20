class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles) 
        piles = deque(piles)
        arr = []
        _sum = 0
        
        while piles:
            x = len(piles) - 2
            d = piles[x]

            piles.popleft()
            piles.pop()
            piles.pop()

            _sum += d
        
        return _sum

            
