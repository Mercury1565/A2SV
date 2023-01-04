class Solution:
    import math
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        checkList = []
        out = []
        for i in points:
            dist = 0
            dist = math.sqrt((i[0])**2 + (i[1])**2)
            checkList.append(dist)
        temp = checkList.copy()
        temp.sort()
        for i in points:
            dist = math.sqrt((i[0])**2 + (i[1])**2)
            if(dist in temp[0:k]):
                out.append(i)
        return out