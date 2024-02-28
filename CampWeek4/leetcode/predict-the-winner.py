class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def fun(arr , turn , p1 , p2):
            if len(arr) == 0:
                return p1 >= p2

            if turn == 1:
                cond_1 = fun(arr[1:] , 2 , p1 + arr[0] , p2)
                cond_2 = fun(arr[:-1] , 2 , p1 + arr[-1] , p2)
                return cond_1 or cond_2
            elif turn == 2:
                cond_1 = fun(arr[1:] , 1 , p1 , p2 + arr[0]) 
                cond_2 = fun(arr[:-1] , 1 , p1 , p2 + arr[-1])
                return cond_1 and cond_2

        return fun(nums , 1 , 0 , 0)


        