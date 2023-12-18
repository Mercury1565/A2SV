class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = 0
        result = ''
        rev = True
        increment = k

        while l < len(s):
            temp = s[l:k]

            if rev:
                result += temp[::-1]
                rev = False
            elif rev == False:
                result += temp
                rev = True
            
            l = k
            k += increment

        return result
                




        