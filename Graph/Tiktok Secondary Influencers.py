# https://www.fastprep.io/problems/tiktok-get-secondary-influencer-sum

from collections import defaultdict, deque

def bfs_farthest(node, n, adj):
    dist = [-1] * (n + 1)
    dist[node] = 0
    queue = deque([node])
    farthest_node = node
    max_dist = 0

    while queue:
        current = queue.popleft()
        for neighbor in adj[current]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[current] + 1
                queue.append(neighbor)
                if dist[neighbor] > max_dist:
                    max_dist = dist[neighbor]
                    farthest_node = neighbor

    return farthest_node, max_dist, dist

def dfs_mark_path(current, parent, adj, target, path_set):
    # 标记从 current 到 target 的路径上的所有节点
    if current == target:
        path_set.add(current)
        return True
    
    for neighbor in adj[current]:
        if neighbor != parent:
            if dfs_mark_path(neighbor, current, adj, target, path_set):
                path_set.add(current)
                return True
    return False

def getSecondaryInfluencerSum(g_nodes, g_from, g_to):
    # Step 1: 创建邻接表表示图
    adj = defaultdict(list)
    for u, v in zip(g_from, g_to):
        adj[u].append(v)
        adj[v].append(u)

    # Step 2: 找到树中的最长路径的两个端点 u 和 v
    # 第一次 BFS 找到一个端点 u
    u, _, _ = bfs_farthest(1, g_nodes, adj)

    # 第二次 BFS 找到最长路径的另一个端点 v
    v, mx, dist_from_u = bfs_farthest(u, g_nodes, adj)

    # Step 3: 递归标记从 u 到 v 的最长路径上的节点
    path_set = set()
    dfs_mark_path(u, -1, adj, v, path_set)

    # Step 4: 计算次级影响者的索引和
    secondary_sum = 0
    for i in range(1, g_nodes + 1):
        if i not in path_set:
            secondary_sum += i

    return secondary_sum

# 示例输入
# g_nodes = 4
# g_from = [1, 1, 2]
# g_to = [2, 3, 4]

# g_nodes = 6
# g_from = [1, 1, 1, 2, 3]
# g_to = [2, 3, 4, 5, 6]

g_nodes = 5
g_from = [1, 1, 2, 2]
g_to = [2, 3, 4, 5]

# 调用函数
print(getSecondaryInfluencerSum(g_nodes, g_from, g_to))
