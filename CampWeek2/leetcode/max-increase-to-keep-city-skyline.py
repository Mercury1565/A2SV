class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_east = []
        max_north = []

        for i in range(len(grid)):
            max_east.append(max(grid[i]))
            temp = 0

            for j in range(len(grid[0])):
                temp = max(temp , grid[j][i])

            max_north.append(temp)

        ssum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ssum += min(max_east[i] , max_north[j]) - grid[i][j]
        
        return ssum                
