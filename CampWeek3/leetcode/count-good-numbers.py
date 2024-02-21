class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9) + 7
        
        pow_5 = (n // 2)
        pow_4 = (n // 2) 

        if n % 2:
            pow_5 += 1   

        return pow(5 , pow_5 , mod) * pow(4 , pow_4 , mod) % mod




        