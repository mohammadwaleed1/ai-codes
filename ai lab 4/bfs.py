# Tree representation as an Adjacency List
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}
def bfs(tree, start, goal):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.append(node)

            if node == goal:
                return visited   # stop when goal found
        for child in tree[node]:
            if child not in visited:
                queue.append(child)

    return "Goal not found"


# Test
print(bfs(tree, 'A' ,'F'))

    
