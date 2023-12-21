class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        for i in range(2 , len(grid)):
            for j in range(3 , len(grid[0]) + 1):
                ssum = 0
                ssum = sum(grid[i - 2][j - 3 : j])
                ssum += grid[i - 1][j - 2]
                ssum += sum(grid[i][j - 3 : j])
                max_sum = max(max_sum , ssum)

        return max_sum
        