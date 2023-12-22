class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = {}
        result = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j in dic:
                    dic[i + j].append(mat[i][j])
                else:
                    dic[i + j] = [mat[i][j]]

        for key in dic:
            if key % 2 == 0:
                result.extend(dic[key][::-1])
            else:
                result.extend(dic[key])

        return result