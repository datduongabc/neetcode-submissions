class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(0, 9)]
        column_set = [set() for _ in range(0, 9)]
        sub_board_set = [set() for _ in range(0, 9)]

        for row in range (0, 9):
            for column in range (0, 9):
                if board[row][column] == ".":
                    continue
                
                sub_board_index = (row // 3) * 3 + (column // 3)

                if board[row][column] in row_set[row] or board[row][column] in column_set[column] or board[row][column] in sub_board_set[sub_board_index]:
                    return False
                else:
                    row_set[row].add(board[row][column])
                    column_set[column].add(board[row][column])
                    sub_board_set[sub_board_index].add(board[row][column])
        
        return True