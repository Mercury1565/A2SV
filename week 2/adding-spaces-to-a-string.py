class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr=[]
        prev=0
        for i in spaces:
            arr.append(s[prev:i])
            prev=i
        arr.append(s[i:])
        return " ".join(arr)