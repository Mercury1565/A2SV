class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def det_box(i , j):
            if i < 3:
                if j < 3:
                    return 'box_1'
                elif j < 6:
                    return 'box_2'
                elif j < 9:
                    return 'box_3'
            elif i < 6:
                if j < 3:
                    return 'box_4'
                elif j < 6:
                    return 'box_5'
                elif j < 9:
                    return 'box_6'
            elif i < 9:
                if j < 3:
                    return 'box_7'
                elif j < 6:
                    return 'box_8'
                elif j < 9:
                    return 'box_9'

        visited_col = defaultdict(set)
        visited_row = defaultdict(set)
        visited_box = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    visited_row[i].add(board[i][j])
                    visited_col[j].add(board[i][j])
                    visited_box[det_box(i , j)].add(board[i][j])

        def backtrack(row , column):
            if row == 9:
                return  True
            if column == 9:
                return backtrack(row + 1 ,0)

            if board[row][column] == '.':
                for value in range(1 ,10):
                    value = str(value)
                    if value in visited_col[column]:
                        continue
                    if value in visited_row[row]:
                        continue

                    current_box = det_box(row , column)
                    
                    if value in visited_box[current_box]:
                        continue
                    
                    board[row][column] = str(value)

                    visited_col[column].add(value)
                    visited_row[row].add(value)
                    visited_box[current_box].add(value)

                    if backtrack(row , column + 1):
                        return True
                    
                    visited_col[column].remove(value)
                    visited_row[row].remove(value)
                    visited_box[current_box].remove(value)

                    board[row][column] = '.'

                return False

            return backtrack(row , column + 1)

                
        backtrack(0 , 0)
                
                            

                            


                



