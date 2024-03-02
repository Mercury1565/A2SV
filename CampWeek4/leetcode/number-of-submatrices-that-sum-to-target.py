class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row , col = len(matrix) , len(matrix[0])

        # First build the sum array
        ssum = []
        for _ in range(row):
            ssum.append([0] * col)

        for i in range(row):
            for j in range(col):
                top , left , corner = 0 , 0 , 0
                if i > 0:
                    top = ssum[i - 1][j]
                if j > 0:
                    left = ssum[i][j - 1]
                if i > 0 and j > 0:
                    corner = ssum[i - 1][j - 1]

                ssum[i][j] = matrix[i][j] + (top + left - corner)

        # Use three pointers and a hashmap to do the rest of the job
        count = 0
        for row_1 in range(len(matrix)):
            for row_2 in range(row_1 , len(matrix)):
                check = defaultdict(int)
                check[0] = 1

                for column in range(col):
                    if row_1 > 0:
                        subArr_sum = ssum[row_2][column] - ssum[row_1 - 1][column]
                    else:
                        subArr_sum = ssum[row_2][column]
                        
                    diff = subArr_sum - target

                    if diff in check:
                        count += check[diff]
                    check[subArr_sum] += 1

        return count

        
                
       
                        