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
def bfs(tree,start, goal,dept):
    visited=[]
    stack=[(start,0)]
    while stack:
        node,level=stack.pop(0)
        if level>dept:
            return None
        if node not in visited:
            print(node)
            visited.append(node)
        if node==goal:
            return visited
        for child in tree[node]:
            if child not in visited:
                stack.append((child, level + 1))

print(bfs(tree,'A','F',1))
