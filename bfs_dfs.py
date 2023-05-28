from queue import Queue

# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = Queue()
    queue.put(start)
    visited.add(start)

    while not queue.empty():
        vertex = queue.get()
        print(vertex)  # Process the vertex

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.put(neighbor)
                visited.add(neighbor)

# Depth-First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)  # Process the vertex

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS traversal:")
bfs(graph, 'A')

print("\nDFS traversal:")
dfs(graph, 'A')




from queue import Queue

def bfs_recursive(graph, queue, visited):
    if queue.empty():
        return

    node = queue.get()
    print(node)  # Process the node

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.put(neighbor)

    bfs_recursive(graph, queue, visited)

# BFS implementation using recursion
def bfs(graph, start):
    visited = set()
    queue = Queue()
    queue.put(start)
    visited.add(start)

    bfs_recursive(graph, queue, visited)

# Example graph represented as an adjacency dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['D', 'E']
}

# Perform BFS starting from node 'A'
bfs(graph, 'A')
