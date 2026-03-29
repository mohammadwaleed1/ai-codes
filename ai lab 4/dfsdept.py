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
def dfs(tree, start, goal,dept):
    visited = []
    queue = [(start,0)]
    while queue:
        node,level = queue.pop()
        if level>dept:
            return None
       
        if node not in visited:
            print(node)
            visited.append(node)

        if node == goal:
            return visited 
        for child in reversed(tree[node]):
            if child not in visited:
                queue.append((child, level + 1))

    return "Goal not found"


# Test
print(dfs(tree, 'A', 'F',1))

    
