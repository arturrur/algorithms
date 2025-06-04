
# Works if graph has no cycles
# Complexity O(|V| + |E|)
def dfs(graph, v, visitados, topoSort):
    visitados[v] = True
    for u in graph[v]:
        if not visitados[u]:
            dfs(graph, u, visitados, topoSort)
    
    topoSort.append(v)

def calldfs(graph, n):
    visitados = [False] * (n+1)
    topoSort = []
    for i in range(1, n+1):
        if not visitados[i]:
            dfs(graph, i, visitados, topoSort)
    
    topoSort = topoSort[::-1]