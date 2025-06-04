def bellman(s, graph, n):
    parent = [-1] * n
    dist = [float("inf")] * n
    dist[s] = 0
    
    for _ in range(n):
        for u in range(n):
            for j in range(len(graph[u])):
                v = graph[u][j]
                if dist[u] + v[1] < dist[v[0]]:
                    dist[v[0]] = dist[u] + v[1]
                    parent[v[0]] = u
    
    # check for negative cycle
    has_negative_cycle = False
    for u in range(n):
        for v in graph[u]:
            if dist[u] + v[1] < dist[v[0]]:
                has_negative_cycle = True
                break
    
    return dist, parent, has_negative_cycle