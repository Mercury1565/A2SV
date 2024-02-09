class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        s = list(map(int , list(s)))

        count = 0
        seeker = 0
    
        for pin in range(n):
            if s[pin] == 0:
                pin += 1
                seeker += 1
            else:
                while seeker < len(s) and s[seeker] == 1:
                    seeker += 1

                if seeker == len(s):
                    break
                else:
                    s[pin] , s[seeker] = s[seeker] , s[pin]
                    count += seeker - pin
   
        return count
            
        