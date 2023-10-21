class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l , r = 0 , len(s1) - 1
    
        freq = {}
        check = {}

        for i in s1:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        while r < len(s2):
            for i in range(l , r + 1):
                if s2[i] in check:
                    check[s2[i]] += 1
                else:
                    check[s2[i]] = 1
            if freq == check:
                return True
            else:
                check = {}
            l += 1
            r += 1
        return False

                           
            
