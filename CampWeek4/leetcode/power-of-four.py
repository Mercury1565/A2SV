class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def fun(n):
            if n == 1:
                return True
            elif n < 1:
                return False

            return fun(n / 4)

        return fun(n)