class Solution:
    def sortSentence(self, s: str) -> str:
        newStr = []
        numSpaces = 0
        for i in s:
            if ord(i) == 32:
                numSpaces += 1
        numWords = numSpaces + 1
        numCheck = 1
        x = len(s) - 1
        while True:
            i = x
            while i >= 0:
                if s[i] == str(numCheck):
                    k = i
                    temp = ""
                    while k > 0:
                        if s[k] == " ":
                            break
                        if s[k - 1] != " ":
                            temp = temp + str(s[k - 1])
                        k -= 1
                i -= 1
            numCheck += 1
            newStr.append(temp)
            if numCheck == numWords + 1:
                break
        output = ""
        for i in newStr:
            for j in range(len(i),0,-1):
                output += i[j - 1]
            output += " "
        return output.strip()