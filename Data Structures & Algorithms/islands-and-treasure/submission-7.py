from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        seen = set()

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        def addTile(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in seen or
                grid[r][c] ==-1
            ):
                return
            
            seen.add((r, c))
            queue.append((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    seen.add((r, c))

        dist = 0


        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()


                if grid[r][c] == 2147483647:
                    grid[r][c] = dist

                for dr, dc in directions:
                    addTile(r + dr, c + dc)

            dist += 1