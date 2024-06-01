class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in map(str, range(1, 10)):
                        if self.isValid(board, i, j, num):
                            board[i][j] = num
                            if self.solve(board):
                                return True
                            board[i][j] = '.'  # backtrack
                    return False  # trigger backtracking
        return True

    def isValid(self, board: List[List[str]], row: int, col: int, num: str) -> bool:
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
            if board[box_row + i // 3][box_col + i % 3] == num:
                return False

        return True