class Solution:
    def numberOfWays(self, s: str) -> int:
        s = list(map(int , list(s)))
        n_01 = []
        n_10 = []

        zero_count = 0
        one_count = 0
        for i in range(len(s) - 1):
            if i == 1:
                n_01 = [s[i] * zero_count]
                if s[i] == 0:
                    n_10 = [one_count]
                else:
                    n_10 = [0]
            elif i != 0:
                n_01.append(n_01[-1] + (s[i] * zero_count))
                if s[i] == 0:
                    n_10.append(n_10[-1] + (one_count))
                else:
                     n_10.append(n_10[-1])

            if s[i] == 0:
                zero_count += 1
            else:
                one_count += 1
      
        zero_values = [0] * (len(s) - 2)
        one_values = s[2:]
        for i in range(2 , len(s)):
            if s[i] == 0:
                zero_values[i - 2] = 1

        result = 0  
        for i in range(len(n_10)):
            result += (n_01[i] * zero_values[i])
            result += (n_10[i] * one_values[i])

        return result
            
            
        