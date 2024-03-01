class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def fun(n , k):
            if n == 1:
                return 0

            is_odd = (k % 2 == 1)
            prev = fun(n - 1 , math.ceil(k/2))

            if prev == 1:
                return 1 if is_odd else 0
            else:
                return 0 if is_odd else 1

        return fun(n , k)
        
        


            
                
           