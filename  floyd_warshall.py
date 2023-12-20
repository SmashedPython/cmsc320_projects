def floyd_warshall(graph):
    num_vertices = len(graph)
    dist_matrix = [row[:] for row in graph]

    # Floyd-Warshall 
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist_matrix[i][j] = min(dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j])

    return dist_matrix


graph = [
    [0, float('inf'), 3, 1, 4],
    [2, 0, -3, float('inf'), 2],
    [float('inf'), float('inf'), 0, 5, float('inf')],
    [float('inf'), -1, float('inf'), 0,float('inf')],
    [float('inf'), float('inf'), 1, 3, 0]
]

result_matrix = floyd_warshall(graph)

print("Shortest Paths Matrix:")
for row in result_matrix:
    print(row)
