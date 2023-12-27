class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row_check = set()
            for j in range(len(board[0])):
                if board[i][j] in row_check and board[i][j] != '.':
                    return False
                row_check.add(board[i][j])
        
        for i in range(len(board[0])):
            column_check = set()
            for j in range(len(board)):
                if board[j][i] in column_check and board[j][i] != '.':
                    #print(board[j][i])
                    return False
                column_check.add(board[j][i])

        #print("&&")
        for st in [(0,0) , (0,3) , (0,6) , (3,0) , (3,3) , (3,6) , (6,0), (6,3),(6,6)]:
            square_check = set()
            for i in range(st[0] , st[0] + 3):
                for j in range(st[1] , st[1] + 3):
                    if board[i][j] in square_check and board[i][j] != '.':
                        return False
                    square_check.add(board[i][j])
          
        return True
    

        
                
        

        