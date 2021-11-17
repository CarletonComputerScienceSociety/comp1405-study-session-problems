vertices = [0, 1, 2, 3]
edges = [(0, 1), (1, 0), (2, 1), (1, 3), (3, 2)]
graph = (vertices, edges)


def create_adjacency_list(graph):
    vertices, edges = graph

    # create adjacency list
    adjacency_list = {}

    # add a black list to each key
    for vertex in vertices:
        adjacency_list[vertex] = []

    # add each edge to the adjacency list
    for edge in edges:
        start, end = edge
        adjacency_list[start].append(end)

    return adjacency_list


def create_adjacency_list_real_list(graph):
    vertices, edges = graph

    # create adjacency list
    adjacency_list = []

    # add a black list to each key
    for _ in vertices:
        adjacency_list.append([])

    # add each edge to the adjacency list
    for edge in edges:
        start, end = edge
        adjacency_list[start].append(end)

    return adjacency_list


def print_2d_list(l):
    for row in l:
        print(row)


def create_adjacency_matrix(graph):
    vertices, edges = graph

    adjacency_matrix = []

    # create a v * v sized matrixof False (template)
    for _ in vertices:
        row = []
        for _ in vertices:
            row.append(False)
        adjacency_matrix.append(row)

    for edge in edges:
        start, end = edge
        adjacency_matrix[start][end] = True

    return adjacency_matrix


print("\nAdjacency List:")
print(create_adjacency_list(graph))
print("\nAdjacency Matrix:")
print_2d_list(create_adjacency_matrix(graph))
