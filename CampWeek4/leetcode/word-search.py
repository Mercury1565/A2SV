class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row , col = len(board) , len(board[0])
        visited = set()

        def backtrack(r , c , i):
            if i == len(word):
                return True

            if (r >= row or r < 0 or
                c >= col or c < 0 or
                word[i] != board[r][c] or
                (r , c) in visited):
                return False

            visited.add((r , c))
            result = (backtrack(r + 1 , c , i + 1) or
                      backtrack(r - 1 , c , i + 1) or
                      backtrack(r , c + 1 , i + 1) or
                      backtrack(r , c - 1 , i + 1))
            visited.remove((r , c))

            return result

        for i in range(row):
            for j in range(col):
                if backtrack(i , j , 0):
                    return True
        return False

            

            

       
        