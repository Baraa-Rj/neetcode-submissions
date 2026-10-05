from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        col = defaultdict(set)
        squares = defaultdict(set)
        for row in range(len(board)):
            for cl in range(len(board[row])):
                if board[row][cl] == ".":
                    continue
                if (board[row][cl] in rows[row] or 
                board[row][cl] in col[cl] or
                board[row][cl] in squares[row//3,cl//3]):
                    return False
                rows[row].add(board[row][cl])
                col[cl].add(board[row][cl])
                squares[row//3,cl//3].add(board[row][cl])

        return True