class Solution:
    def freqAlphabets(self, s: str) -> str:
        hashMap = {}
        result = []
        
        for i in range(1,27):
            hashMap[i] = chr(i + 96)
        
        for i in range(len(s)):
            if s[i] == '#':
                result.pop()
                result.pop()
              
                result.append(hashMap[int(s[i - 2 : i])])
                pole = i + 1
                continue
            
            
            if s[i] == '0':
                result.append(" ")
                continue
            result.append(hashMap[int(s[i])])
                
        return "".join(result)


        