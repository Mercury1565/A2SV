class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        result = []

        for candy in candies:
            result.append(candy + extraCandies >= max_candy)
        
        return result