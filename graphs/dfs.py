
# Complexity O(|V| + |E|)
def dfs(graph, v, visitados):
    visitados[v] = 1
    for u in graph[v]:
        if not visitados[u]:
            dfs(graph, u, visitados)