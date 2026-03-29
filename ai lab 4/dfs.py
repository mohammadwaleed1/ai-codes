# Tree Representation
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
def dfs(tree, start, goal):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop()
        if node not in visited:
            print(node)
            visited.append(node)

            if node == goal:
                return visited   # stop when goal found

        for child in reversed(tree[node]):
            if child not in visited:
                queue.append(child)


    return "Goal not found"


# Test
print(dfs(tree, 'A', 'F'))

    
