class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = []
        for point in points:
            x.append(point[0])
        x.sort()

        max_arr = 0
        for i in range(len(x) - 1):
            max_arr = max(max_arr , x[i + 1] - x[i])
        return max_arr
        