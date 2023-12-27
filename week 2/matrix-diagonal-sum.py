class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ssum = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i - j == 0 or i + j == (len(mat) - 1):
                    ssum += mat[i][j]
        
        return ssum

        