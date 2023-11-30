class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num / 3 == num // 3:
            var = num // 3 
            return [var - 1 , var , var + 1]
        return []
        