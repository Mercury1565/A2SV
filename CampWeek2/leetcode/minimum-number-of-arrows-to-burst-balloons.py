class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ref = points[0]
        count = 0

        for i in range(1 , len(points)):
            ref[0] = max(points[i][0] , ref[0])
            ref[1] = min(points[i][1] , ref[1])
            if ref[0] > ref[1]:
                count += 1
                ref = points[i]

        return count + 1



        