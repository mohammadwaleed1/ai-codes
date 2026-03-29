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
def DLS(tree, start, goal, depth_limit):
    stack = [(start, 0)] 
    visited = []

    while stack:
        node, depth = stack.pop()

        if depth > depth_limit:
            continue

        print(node, f"(depth={depth})")

        if node not in visited:
            visited.append(node)

        if node == goal:
            return visited 
        for child in reversed(tree[node]):
            if child not in visited:
                stack.append((child, depth + 1))

    return None  
def IDS(tree, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\n IDS iteration with depth limit = {depth} ---")
        result = DLS(tree, start, goal, depth)
        if result:
            print(f"\nGoal '{goal}' found at depth {depth}!")
            return result
    return "Goal not found"
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'A'], 
    'C': ['F', 'G'],
    'D': ['H', 'B'],  
    'E': ['C'],          
    'F': ['I'],
    'G': ['C'],            
    'H': [],
    'I': ['A']        
}

result = IDS(tree, 'A', 'F', 3)
print("\nVisited path:", result)
