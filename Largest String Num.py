class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numStr = []
        string = ""
        for i in nums:
            numStr.append(str(i))
        while True:
            max = int(numStr[0])
            for i in numStr:
                if i[0] > str(max)[0]:
                    max = int(i)
                    maxStr = str(i)
                elif i[0] == str(max)[0]:
                    if int(i + str(max)) > int(str(max) + i):
                        max = int(i)
                        maxStr = str(i)
                    else:
                        maxStr = str(max)
            string += maxStr
            numStr.remove(maxStr)
            if numStr == []:
                break
        for i in string:
            temp = i
            if i != "0":
                break
        if temp == "0":
            return str(0)
        return string

