class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        seen = set()
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        minute = 0
        fresh = 0

        ## Start queue with a rotten fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append([r,c])
                    seen.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        def addfruits(r,c):
            nonlocal fresh
            if r<0 or r == ROWS or c<0 or c == COLS or grid[r][c]!=1 or (r,c) in seen:
                return
            fresh -=1
            queue.append([r,c])
            seen.add((r,c)) 
            grid[r][c] = 2 

        ## Go through queue
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for r_, c_ in directions:
                    addfruits(r+r_,c+c_)
            minute +=1
                
        return minute if fresh == 0 else -1
                
