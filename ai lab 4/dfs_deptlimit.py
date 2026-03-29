tree = [
    ['B', 'C'],  # A
    ['D', 'E'],  # B
    ['F', 'G'],  # C
    ['H'],       # D
    [],          # E
    ['I'],       # F
    [],          # G
    [],          # H
    []           # I
]

# Keep a separate list for node names in order
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
def dfs(tree, nodes, start, goal, dept):
    visited = []
    stack = [(start, 0)]  # start = 'A'

    while stack:
        node, level = stack.pop()

        if level > dept:
            continue

        if node not in visited:
            print(node)
            visited.append(node)

        if node == goal:
            return visited

        # Get children using nodes index
        children = tree[nodes.index(node)]
        for child in reversed(children):
            stack.append((child, level + 1))

    return "Goal not found"


# Test
print(dfs(tree, nodes, 'A', 'F', 2))
