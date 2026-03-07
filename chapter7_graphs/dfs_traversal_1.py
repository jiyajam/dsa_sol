def DFS(graph, u, visited=None):
    """
    Perform Depth-First Search of the undiscovered portion of the graph starting at Vertex u.

    Returns a dictionary where:
        key   -> vertex
        value -> vertex from which it was discovered
    """
    # First call: initialize dictionary
    if visited is None:
        visited = {u: None}

    # Explore neighbors
    for v in graph._adj_map[u]:
        if v not in visited:
            visited[v] = u
            DFS(graph, v, visited)

    return visited