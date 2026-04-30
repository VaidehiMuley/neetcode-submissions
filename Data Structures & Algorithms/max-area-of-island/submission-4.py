class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        areas = []
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        curr_area = 0

        def dfs(r,c):
            ## Base case
            if (r<0 or c < 0 or 
                r >= ROWS or c >= COLS or
                grid[r][c] == 0):
                return 0

            curr_area = 1
            grid[r][c] = 0
            for i, j in directions:
                curr_area += dfs(r+i, c+j)
            return curr_area
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    ## First cell of island detected
                    areas.append(dfs(r, c))

        return max(areas) if areas else 0
        