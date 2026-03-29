# # Tree Representation
# tree = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': ['H'],
#     'E': [],
#     'F': ['I'],
#     'G': [],
#     'H': [],
#     'I': []
# }

# # Depth-Limited DFS
# def DLS(tree, start, goal, depth_limit):
#     stack = [(start, 0)]   # node with current depth
#     visited = []

#     while stack:
#         node, depth = stack.pop()

#         if depth > depth_limit:
#             continue

#         print(node, f"(depth={depth})")  # show traversal

#         if node not in visited:
#             visited.append(node)

#         if node == goal:
#             return visited  # goal found

#         # push children in reversed order to maintain left-to-right DFS
#         for child in reversed(tree[node]):
#             if child not in visited: 
#                 stack.append((child, depth + 1))

#     return None  # goal not found within this depth

# # Iterative Deepening Search
# def IDS(tree, start, goal, max_depth):
#     for depth in range(max_depth + 1):
#         print(f"\n--- IDS iteration with depth limit = {depth} ---")
#         result = DLS(tree, start, goal, depth)
#         if result:
#             print(f"\nGoal '{goal}' found at depth {depth}!")
#             return result
#     return "Goal not found"

# # Test IDS
# result = IDS(tree, 'A', 'F', 3)
# print("\nVisited path:", result)


#code for never ending ids until goal found
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

# Depth-Limited DFS
def DLS(tree, start, goal, depth_limit):
    stack = [(start, 0)]   # node with current depth
    visited = []

    while stack:
        node, depth = stack.pop()

        if depth > depth_limit:
            continue

        print(node, f"(depth={depth})")  # show traversal

        if node not in visited:
            visited.append(node)

        if node == goal:
            return visited  # goal found

        # push children in reversed order to maintain left-to-right DFS
        for child in reversed(tree[node]):
            if child not in visited: 
                stack.append((child, depth + 1))

    return None  # goal not found within this depth

# Iterative Deepening Search
def IDS(tree, start, goal):
    depth=0
    while True:
        print(f"\n--- IDS iteration with depth limit = {depth} ---")
        result = DLS(tree, start, goal, depth)
        if result:
            print(f"\nGoal '{goal}' found at depth {depth}!")
            return result
        depth+=1
    return "Goal not found"
     

# Test IDS
result = IDS(tree, 'A', 'F')
print("\nVisited path:", result)