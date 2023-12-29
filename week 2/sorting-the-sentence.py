class Solution:
    def sortSentence(self, s: str) -> str:
        dic = {}
        result = ''
        s = s.split()

        for word in s:
            dic[int(word[-1])] = word[:-1]

        for i in range(1,10):
            if i in dic:
                result += dic[i] + ' '
            
        return result.rstrip()
        