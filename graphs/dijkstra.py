import heapq

# Using mean-heap as priority queue, ony works if all edges are positive
# Complexity O((|V| + |E|) * lg(V))
def dijkstra(s, graph, v):
    dist = [float('inf')] * v
    parent = [-1] * v
    dist[s] = 0

    pq = []
    heapq.heappush(pq, (dist[s], s))  # (distância, vértice)

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue
        
        for v in graph[u]:
            vert, weight = v
            if dist[u] + weight < dist[vert]:
                dist[vert] = dist[u] + weight
                parent[vert] = u
                heapq.heappush(pq, (dist[vert], vert))

    return dist, parent