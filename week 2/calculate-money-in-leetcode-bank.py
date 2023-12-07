class Solution:
    def totalMoney(self, n: int) -> int:
        result = 0
        count = 0
        monday = 1

        for _ in range(n):
            if count == 7:
                count = 0
                monday += 1
            
            result += (count + monday)
            count += 1

        return result
            


        