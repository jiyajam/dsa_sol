def BFS(graph, start):
    """
    Perform Breadth-First Search starting at vertex start.

    Returns a dictionary where:
        key   -> vertex
        value -> vertex from which it was discovered
    """
    visited = {start: None}
    queue = [start]   # use list as queue

    while queue:
        u = queue.pop(0)   # dequeue (FIFO)

        for v in graph._adj_map[u]:
            if v not in visited:
                visited[v] = u
                queue.append(v)

    return visited