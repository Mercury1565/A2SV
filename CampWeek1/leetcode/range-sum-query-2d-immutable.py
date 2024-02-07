class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # The padding Process
        arr = []
        arr.append([0] * (len(matrix[0]) + 1))
        
        for row in matrix:
            arr.append([0] + row)

        # Prefix Sum Calculation
        for i in range(1 , len(arr)):
            for j in range(1 , len(arr[0])):
                arr[i][j] = arr[i][j - 1] + arr[i - 1][j] + arr[i][j] - arr[i- 1][j - 1] 
        self.arr = arr
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # ssum = self.arr[row2][col2]
        # ssum -= self.arr[row2][col1 - 1]
        # ssum -= self.arr[row1 - 1][col2]
        # ssum += self.arr[row1 - 1][col1 - 1]
        # All this shit is off by one because of the padding, hence...
        ssum = self.arr[row2 + 1][col2 + 1]
        ssum -= self.arr[row2 + 1][col1]
        ssum -= self.arr[row1][col2 + 1]
        ssum += self.arr[row1][col1]

        return ssum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)