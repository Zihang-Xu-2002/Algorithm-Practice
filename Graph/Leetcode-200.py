from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return
        n = len(grid[0])
        m = len(grid)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(r,c):
            #queue = deque([(r,c)])
            queue = [(r,c)]
            grid[r][c] = "0"
            while queue:
                r_val, c_val = queue.pop(0)
                for dr, dc in directions:
                    nr = r_val + dr
                    nc = c_val + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))
        counter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i,j)
                    counter += 1
        return counter
"""practice summary
BFS is a good way. But remember to mark the 
visited node as "0" to avoid infinite loop.
"""