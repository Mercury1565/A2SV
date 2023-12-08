class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        checkSet = set()
        flag = set()

        for interval in ranges:
            checkSet.update(list(n for n in range(interval[0] , interval[1] + 1)))
        
        for j in range(left , right + 1):
            flag.add(j)

        return flag <= checkSet 
        