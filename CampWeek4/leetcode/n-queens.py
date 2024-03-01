class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []

        def backtrack(row , visited_col , visited_diagonal_1 , visited_diagonal_2 , path):

            if len(path) >= n:
                if len(path) == n:
                    answer.append(path[:])
                return

            for col in range(n):
                if col in visited_col:
                    continue
                if row - col in visited_diagonal_1:
                    continue
                if row + col in visited_diagonal_2:
                    continue

                s = ['.'] * n
                s[col] = 'Q'
                path.append(s)

                visited_col.add(col)
                visited_diagonal_1.add(row - col)
                visited_diagonal_2.add(row + col)

                backtrack(row + 1 , visited_col , visited_diagonal_1 , visited_diagonal_2 , path)

                visited_col.remove(col)
                visited_diagonal_1.remove(row - col)
                visited_diagonal_2.remove(row + col)

                path.pop()

        backtrack(0  , set() , set() , set() , [])
        for ans in answer:
            for k in range(len(ans)):
                ans[k] = ''.join(ans[k])
        return answer

                
                

