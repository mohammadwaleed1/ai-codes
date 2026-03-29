# Tree Representation
tree = {
    'A': ['B', 'C','D'],
    'B': ['E', 'F','C'],
    'C': ['B','F'],
    'D': ['G'],
    'E': ['H'],
    'F': ['I'],
    'G': [],
    'H': [],
}
def dfs(tree, start,dept):
    visited = []
    queue = [(start,0)]
    while queue:
        node,level = queue.pop()
        if level>dept:
            continue
        if node not in visited:
            print(node)
            visited.append(node)

        for child in reversed(tree[node]):
            if child not in visited:
                queue.append((child,level+1))

    return visited


# Test
print(dfs(tree, 'A',2))

    
