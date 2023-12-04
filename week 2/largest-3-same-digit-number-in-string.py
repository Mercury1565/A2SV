class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = 0
        flag = True

        for r in range(3, len(num) + 1):
            if len(set(num[r - 3 : r])) == 1:
                flag = False
                result = max(result , int(num[r - 3 : r]))
       

        return '' if flag else'0' * (3 - len(str(result))) + str(result)
        