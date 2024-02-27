class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fun(x , n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            result = fun(x , n // 2)
            result *= result
            
            return x * result if n % 2 else result

        output = fun(x , abs(n))
        return output if n >= 0 else 1 / output
        