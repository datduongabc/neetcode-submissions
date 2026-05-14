class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxSet = [set() for _ in range(9)]

        for row_idx in range(9):
            existed1 = set()
            existed2 = set()
            for column_idx in range(9):
                element1 = board[row_idx][column_idx]
                if element1 != ".":
                    # Check rows validation
                    if element1 not in existed1:
                        existed1.add(element1)
                    else:
                        return False

                    # Check boxes validation
                    box_idx = (row_idx // 3) * 3 + (column_idx // 3)
                    if element1 not in boxSet[box_idx]:
                        boxSet[box_idx].add(element1)
                    else:
                        return False
                
                # Check columns validation
                element2 = board[column_idx][row_idx]
                if element2 != ".":
                    if element2 not in existed2:
                        existed2.add(element2)
                    else:
                        return False

        return True