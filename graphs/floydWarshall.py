def floyd(matrix, pred):
    V = len(matrix)
    
    for i in range(V):
        for j in range(V):
            pred[i][j] = i
    
    # at each step matrix[i][j] is the smallest path from i to j using the vertices [0...k] 
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    pred[i][j] = pred[k][j]
                    
def printPath(pred, i, j):
    if i != j: 
        printPath(pred, i, pred[i][j])
    print(f" {j}")