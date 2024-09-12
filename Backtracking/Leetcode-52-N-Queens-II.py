class Solution:
    def isValid(self,row, col,chessboard,n):
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False  # 左上方向已经存在皇后，不合法
            i -= 1
            j -= 1

        # 检查 135 度角是否有皇后
        i, j = row - 1, col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == 'Q':
                return False  # 右上方向已经存在皇后，不合法
            i -= 1
            j += 1

        return True  # 当前位置合法
        
    def totalNQueens(self, n: int) -> int:
        result = []
        chessboard = ['.' * n for _ in range(n)]  # 初始化棋盘

        def backtracking(n, row, chessboard,result):
            if row == n :
                result.append(chessboard)
                return
            for col in range(n):
                if self.isValid(row,col,chessboard,n):
                    chessboard[row] = chessboard[row][:col]+ 'Q' + chessboard[row][col+1:]
                    backtracking(n,row+1,chessboard,result)
                    chessboard[row] = chessboard[row][:col]+ '.' + chessboard[row][col+1:]
        backtracking(n,0,chessboard,result)
        return len(result)
            
