from queue import PriorityQueue

# 1. Graph with Edge Costs (ignored by Greedy BFS, but kept for structure)
graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'D': [], 
    'E': [], 
    'F': [('I', 6)], 
    'G': [],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'J': [], 
    'K': [], 
    'L': [], 
    'M': []
}
# 2. Heuristic Table (Estimated cost to reach Goal 'I')
heuristic = {
    'S': 10, 'A': 7, 'B': 6, 'C': 5, 
    'D': 4, 'E': 7, 'F': 3, 'G': 6, 
    'H': 2, 'I': 0, 'J': 4, 'K': 1, 'L': 10, 'M': 2
}

def a_star_search(graph, start, goal):
    visited = set()
    pq = PriorityQueue()
    came_from = {start: None}
    # PriorityQueue stores: (f_cost, g_cost, node)
    # f = g + h. At the start, g is 0.
    pq.put((0 + heuristic[start], 0, start)) 

    while not pq.empty():
        # Pop the node with the lowest TOTAL estimated cost (f)
        f_val, g_val, node = pq.get()

       
        if node == goal:
            # reconstruct path
            path = []
            n = goal
            while n is not None:
                path.append(n)
                n = came_from[n]
            path.reverse()
            print(f"\nPath Found : {path}")
            print(f"Steps      : {len(path)-1}")
            return

            # Since your graph is a list of tuples, we unpack directly:
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                # g = path cost from start to parent + cost of this new edge
                new_g = g_val + edge_cost
                # f = g + neighbor's heuristic
                new_f = new_g + heuristic[neighbor]
                    
                pq.put((new_f, new_g, neighbor))

    print("\nGoal not reachable!")
    return False

print("A* Search Path:")
a_star_search(graph, 'S', 'I')