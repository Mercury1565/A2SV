class Solution:
    def smallestNumber(self, num: int) -> int:  
        def compare(n1 , n2):
            return n1 + n2 > n2 + n1

        num = list(str(num))
        for i in range(len(num)):
            for j in range(1 , len(num) - i):
                if compare(num[j - 1] , num[j]):
                    num[j - 1] , num[j] = num[j] , num[j - 1]
        #print(num)
        if num[0] == '-':
            num[1:] = num[:0:-1]
        elif '0' in num:
            for i in range(1 , len(num)):
                if num[i] != '0':
                    break
            num[0] , num[i] = num[i] , num[0]   

        return int(''.join(num))


        