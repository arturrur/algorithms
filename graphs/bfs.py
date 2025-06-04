from collections import deque


# Complexity O(|V| + |E|)
def bfs(graph, s, n):
    d = [float('inf')] * n
    d[s] = 0
    q = deque()
    q.append(s)
    while q:
        v = q.popleft()
        for u in graph[v]:
            if d[u] == float('inf'):
                d[u] = d[v] + 1
                q.append(u)
    return d