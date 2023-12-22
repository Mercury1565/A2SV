class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        
        for i in range(len(matrix) - 1):
            c1 = [i , i]
            c2 = [i , n]
            c3 = [n , n ]
            c4 = [n, i]

            for _ in range(n - i):
                matrix[c1[0]][c1[1]] ,  matrix[c2[0]][c2[1]] =  matrix[c2[0]][c2[1]] ,  matrix[c1[0]][c1[1]]
                matrix[c1[0]][c1[1]] ,  matrix[c3[0]][c3[1]] =  matrix[c3[0]][c3[1]] ,  matrix[c1[0]][c1[1]]
                matrix[c1[0]][c1[1]] ,  matrix[c4[0]][c4[1]] =  matrix[c4[0]][c4[1]] ,  matrix[c1[0]][c1[1]]
                
                c1[1] += 1
                c2[0] += 1
                c3[1] -= 1
                c4[0] -= 1

            n -= 1

        return matrix
