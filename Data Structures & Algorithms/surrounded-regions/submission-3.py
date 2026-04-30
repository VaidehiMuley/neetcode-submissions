class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        def capture(r,c):
            if (r<0 or r== ROWS or 
                c <0 or c==COLS or
                board[r][c]!= 'O'):
                return
            board[r][c] = 'T'
            for r_,c_ in directions:
                capture(r+r_, c+c_)

        ## Check for the first and last row
        for c in range(COLS):
            if board[0][c] == 'O':
                capture(0,c)
            if board[ROWS-1][c] == 'O':
                capture(ROWS-1,c)

        ## Check for first and last cols
        for r in range(ROWS):
            if board[r][0] == 'O':
                capture(r,0)
            if board[r][COLS-1] == 'O':
                capture(r, COLS-1)

        
        ## Convert T to "O"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

        