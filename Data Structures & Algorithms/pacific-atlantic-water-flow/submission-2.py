class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        prevHeight = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        ## Water can only flow from water to the block if height is equal or greater than prev
        def dfs(r,c,prevHeight,visit):
            if (r < 0 or r == ROWS or c<0 or c ==COLS or heights[r][c] < prevHeight or (r,c) in visit):
                return
            visit.add((r,c))
            ## Do the same for neighbours
            for r_,c_ in directions:
                dfs(r+r_, c+c_, heights[r][c],visit)


        ## start from the first row and the last row
        for c in range(COLS):
            dfs(0,c,heights[0][c], pac)
            dfs(ROWS-1,c, heights[ROWS-1][c], atl)

        ## start from leftmost and rightmost col
        for r in range(ROWS):
            dfs(r,0, heights[r][0], pac)
            dfs(r,COLS-1, heights[r][COLS-1], atl)

        ## Check cells which are in both pac and atl
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])  

        return res


