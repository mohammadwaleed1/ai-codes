#task 1 DLS
# class Environment:
#     def __init__(self, graph):
#         self.graph = graph

#     def get_percept(self, node):
#         return self.graph.get(node, [])

# class Agent:
#     def __init__(self, goal):
#         self.goal = goal

#     def dfs_search(self, env, start,dept):
#         visited = []
#         queue = [(start,0)]

#         while queue:
#             node,level = queue.pop()
#             print("Agent visiting:", node)

#             if level > dept:
#                 return None
#             if node not in visited:
#                 visited.append(node)

#                 if node == self.goal:
#                     return visited
#             for child in reversed(env.get_percept(node)):
#                 queue.append((child,level+1))

#         return "Goal Not Found"

# def simulate(environment, agent, start,dept):
#     print("Simulation Started")
#     result = agent.dfs_search(environment, start,dept)
#     print("Simulation Ended")
#     print("Result:", result)

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
# env = Environment(tree)
# agent = Agent('F')
# simulate(env, agent, 'A',1)

#TASK 1 UCS
# class Environment:
#     def __init__(self, graph):
#         self.graph = graph

#     def get_percept(self, node):
#         # Returns neighbors and their costs
#         return self.graph.get(node, {})
# class Agent:
#     def __init__(self, goal):
#         self.goal = goal

#     def ucs_search(self, env, start):
#         frontier = [(start, 0)]  
#         visited = set()
#         cost_so_far = {start: 0}
#         came_from = {start: None}

#         while frontier:
#             frontier.sort(key=lambda x: x[1])
#             current_node, current_cost = frontier.pop(0)

#             if current_node in visited:
#                 continue
#             visited.add(current_node)

#             print(f"Agent visiting: {current_node}, cost so far: {current_cost}")

#             if current_node == self.goal:
#                 path = []
#                 node = current_node
#                 while node is not None:
#                     path.append(node)
#                     node = came_from[node]
#                 path.reverse()
#                 print(f"Goal found! Path: {path}, Total Cost: {current_cost}")
#                 return path, current_cost
#             for neighbor, cost in env.get_percept(current_node).items():
#                 new_cost = current_cost + cost
#                 if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
#                     cost_so_far[neighbor] = new_cost
#                     came_from[neighbor] = current_node
#                     frontier.append((neighbor, new_cost))

#         print("Goal not found")
#         return None

# def simulate(environment, agent, start):
#     print("Simulation Started")
#     result = agent.ucs_search(environment, start)
#     print("Simulation Ended")
#     return result
# graph = {
#     'A': {'B': 1, 'C': 2},
#     'B': {'D': 4, 'E': 3},
#     'C': {'F': 1, 'G': 5},
#     'D': {'H': 2},
#     'E': {},
#     'F': {'I': 6},
#     'G': {},
#     'H': {},
#     'I': {}
# }
# env = Environment(graph)
# agent = Agent('I')
# simulate(env, agent, 'A')

#TASK 2

def UCS(graph, start, goal):
    frontier = [(start, 0, [start])]
    visited = {} 

    while frontier:
        min_index = 0
        for i in range(1, len(frontier)):
            if frontier[i][1] < frontier[min_index][1]:
                min_index = i

        current_node, current_cost, path = frontier.pop(min_index)

        if current_node in visited and current_cost >= visited[current_node]:
            continue
        visited[current_node] = current_cost
        if current_node == goal:
            print(f"Goal found! Path: {path}, Total cost: {current_cost}")
            return path, current_cost

        for neighbor, cost in graph.get(current_node, {}).items():
            new_cost = current_cost + cost
            frontier.append((neighbor, new_cost, path + [neighbor]))

    print("Goal not found")
    return None

graph = {
    1: {2: 10, 3: 15},
    2: {4: 25, 3: 35, 1: 10},
    3: {1: 15, 2: 35, 4:30},
    4: {1: 20, 2: 25, 3:30},
}
UCS(graph,1,4)

#TASK 3
# Tree Representation
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
# def DLS(tree, start, goal, depth_limit):
#     stack = [(start, 0)] 
#     visited = []

#     while stack:
#         node, depth = stack.pop()

#         if depth > depth_limit:
#             continue

#         print(node, f"(depth={depth})")

#         if node not in visited:
#             visited.append(node)

#         if node == goal:
#             return visited 
#         for child in reversed(tree[node]):
#             stack.append((child, depth + 1))

#     return None  
# def IDS(tree, start, goal, max_depth):
#     for depth in range(max_depth + 1):
#         print(f"\n IDS iteration with depth limit = {depth} ---")
#         result = DLS(tree, start, goal, depth)
#         if result:
#             print(f"\nGoal '{goal}' found at depth {depth}!")
#             return result
#     return "Goal not found"
# result = IDS(tree, 'A', 'F', 3)
# print("\nVisited path:", result)

# # graph representation
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
#code for forever loop until goal found
#def IDS(tree, start, goal):
    # depth = 0
    
    # while True:   # No fixed max depth
    #     print(f"\n--- IDS iteration with depth limit = {depth} ---")
    #     result = DLS(tree, start, goal, depth)
        
    #     if result:
    #         print(f"\nGoal '{goal}' found at depth {depth}!")
    #         return result
        
    #     depth += 1