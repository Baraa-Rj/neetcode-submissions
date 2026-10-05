from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]

        for i in range(9):  # rows
            for j in range(9):  # columns
                num = board[i][j]
                if num != '.':
                    box_index = (i // 3) * 3 + (j // 3)
                    
                    if num in rows[i]:
                        return False
                    if num in cols[j]:
                        return False
                    if num in boxes[box_index]:
                        return False
                    
                    rows[i][num] = True
                    cols[j][num] = True
                    boxes[box_index][num] = True
        
        return True
