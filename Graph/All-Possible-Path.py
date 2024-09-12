# https://kamacoder.com/problempage.php?pid=1170

import sys
from collections import defaultdict

def all_paths(n, edges):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
    
    result = []
    
    def dfs(node, path):
        if node == n:
            result.append(path[:])
            return
        for neighbor in graph[node]:
            path.append(neighbor)
            dfs(neighbor, path)
            path.pop()
    dfs(1,[1])
    
    if result:
        for path in result:
            print(" ".join(map(str, path)))
    else:
        print(-1)


n, m = map(int, input().split())
edges= []
for i in range(m):
    a,b = map(int, input().split())
    edges.append([a,b])
all_paths(n, edges)