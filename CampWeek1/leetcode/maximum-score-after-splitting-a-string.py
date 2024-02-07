class Solution:
    def maxScore(self, s: str) -> int:
        zeros = []
        ones = []

        for i in range(len(s) - 1):
            if s[i] == '0':
                if zeros:
                    zeros.append(zeros[-1] + 1)
                else:
                    zeros = [1]
            else:
                if zeros:
                    zeros.append(zeros[-1])
                else:
                    zeros = [0]

        for j in range(len(s) - 1 , 0 , -1):
            if s[j] == '1':
                if ones:
                    ones.append(ones[-1] + 1)
                else:
                    ones = [1]
            else:
                if ones:
                    ones.append(ones[-1])
                else:
                    ones = [0]
        ones = ones[::-1]

        result = 0
        for i in range(len(zeros)):
            result = max(result , ones[i] + zeros[i])
        
        return result
        