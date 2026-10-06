class Solution:
    def isValidSudoku(self,board: List[List[str]]) -> bool:
        my_set = set()
        for row in board:
            for n in row:
                if n != ".":
                    if n in my_set:
                        return False
                    else:
                        my_set.add(n)
            my_set = set()
        for col in zip(*board):
            for n in col:
                if n != ".":
                    if n in my_set:
                        return False
                    else:
                        my_set.add(n)
            my_set = set()
        my_set = set()
        for block_row in range(0, 9, 3):
            for block_column in range(0, 9, 3):
                for i in range(block_row, block_row + 3):
                    for j in range(block_column, block_column + 3):
                        if board[i][j] != ".":
                            if board[i][j] in my_set:
                                return False
                            else:
                                my_set.add(board[i][j])
                my_set = set()
        return True

            