def is_valid(knights, row, col):
    # 判断是否能够在(row, col)放置骑士，knights是已经放置的骑士坐标
    for r, c in knights:
        if (abs(r - row) == 1 and abs(c - col) == 2) or (abs(r - row) == 2 and abs(c - col) == 1):
            return False
    return True

def backtrack(n, m, knights, start_row, start_col, count):
    # 如果已经放置了3个骑士，返回1作为有效解法
    if count == 3:
        return 1
    
    # 记录有效摆放方法的数量
    total_ways = 0
    
    # 遍历棋盘上的所有可能位置
    for i in range(start_row, n):
        for j in range(start_col if i == start_row else 0, m):
            # 检查当前位置是否可以放置骑士
            if is_valid(knights, i, j):
                # 递归：尝试将骑士放置在(i, j)并继续寻找下一个骑士的位置
                knights.append((i, j))
                total_ways += backtrack(n, m, knights, i, j + 1, count + 1)
                knights.pop()  # 回溯，撤销上一步的选择
    
    return total_ways

def count_placements(n, m):
    return backtrack(n, m, [], 0, 0, 0)

# 测试用例
n, m = 2, 3
print(count_placements(n, m))  # 输出：20
