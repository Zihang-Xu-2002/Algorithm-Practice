from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m = len(board)
        n = len(board[0])
        def bfs(r,c):
            queue = [(r,c)]
            queue_all_nodes = [(r,c)]
            board[r][c] = "XX"
            surround = True
            if r == 0 or r == m-1 or c == 0 or c == n-1:
                surround = False
            while queue:
                nr, nc = queue.pop(0)
                for br, bc in directions:
                    new_nr = nr + br
                    new_nc = nc + bc
                    if 0 <= new_nr < m and 0 <= new_nc < n and board[new_nr][new_nc] == "O":
                        board[new_nr][new_nc] = "XX"
                        queue.append((new_nr,new_nc))
                        queue_all_nodes.append((new_nr,new_nc))
                        if new_nr == 0 or new_nr == m-1 or new_nc == 0 or new_nc == n-1:
                            surround = False
            if not surround:
                for i,j in queue_all_nodes:
                    board[i][j] = "OX"
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    bfs(i,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "OX":
                    board[i][j] = "O"
                elif board[i][j] == "XX":
                    board[i][j] = "X"