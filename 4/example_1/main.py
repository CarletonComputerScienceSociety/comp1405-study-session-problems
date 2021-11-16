vertices = [0, 1, 2, 3]
edges = [(0, 1), (1, 0), (2, 1), (1, 3), (3, 2)]
graph = (vertices, edges)

# print python 2d list as a 2d array
def print_2d_list(l):
    for row in l:
        print(row)


def create_adjacency_list(graph):
    # decompress graph
    vertices, edges = graph

    # create adjacency list
    adjecency_list = {}

    # add a blank list at each key
    for vertex in vertices:
        adjecency_list[vertex] = []

    # add edges to the list
    for edge in edges:
        start, end = edge
        adjecency_list[start].append(end)

    # return the list
    return adjecency_list


def create_adjacency_matrix(graph):
    # decompress graph
    vertices, edges = graph

    # create adjacency matrix
    adjacency_matrix = []

    # create a vxv sized matrix of False
    for _ in vertices:
        row = []
        for _ in vertices:
            row.append(False)
        adjacency_matrix.append(row)

    # replace False with True where edges exist
    for edge in edges:
        start, end = edge
        adjacency_matrix[start][end] = True

    # return the matrix
    return adjacency_matrix


# create adjacency list and matrix
adjacency_list = create_adjacency_list(graph)
adjacency_matrix = create_adjacency_matrix(graph)

# print adjacency list
print("\nAdjacency List:")
print(adjacency_list)
print("\nAdjacency Matrix:")
print_2d_list(adjacency_matrix)
