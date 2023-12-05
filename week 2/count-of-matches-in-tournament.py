class Solution:
    def numberOfMatches(self, n: int) -> int:
        result = 0

        while n > 1:
            if n % 2 == 0:
                result += int(n // 2)
                n /= 2
            else:
                result += int(n // 2)
                n = int(n // 2) + 1
         
        
        return result
                

        