class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr=[]
        p=0
        for i in spaces:
            arr.append(s[p:i])
            p=i
        arr.append(s[i:])
        return " ".join(arr)
