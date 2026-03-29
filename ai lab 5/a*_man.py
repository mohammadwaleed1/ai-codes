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
coordinates = {
    'S': (0, 0),
    'A': (1, 2),
    'B': (2, 1),
    'C': (1, 1),
    'D': (2, 3),
    'E': (3, 2),
    'F': (4, 1),
    'G': (4, 2),
    'H': (2, 0),
    'I': (3, 0),   # ← goal
    'J': (3, 1)
}

def a_star_search(graph, start, goal):
    visited = set()
    pq = PriorityQueue()
    
    def manhattan(node, goal):
        x1, y1 = coordinates[node]
        x2, y2 = coordinates[goal]
        return abs(x1 - x2) + abs(y1 - y2)
    # PriorityQueue stores: (f_cost, g_cost, node)
    # f = g + h. At the start, g is 0.
    h= manhattan(start, goal)
    pq.put((0 + h, 0, start)) 

    while not pq.empty():
        # Pop the node with the lowest TOTAL estimated cost (f)
        f_val, g_val, node = pq.get()

        if node not in visited:
            print(node, end=' -> ')
            visited.add(node)

            if node == goal:
                print("\nGoal reached!")
                return True

            # Since your graph is a list of tuples, we unpack directly:
            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    # g = path cost from start to parent + cost of this new edge
                    new_g = g_val + edge_cost
                    # f = g + neighbor's heuristic
                    h=manhattan(neighbor,goal)
                    new_f = new_g + h
                    
                    pq.put((new_f, new_g, neighbor))

    print("\nGoal not reachable!")
    return False

print("A* Search Path:")
a_star_search(graph, 'S', 'I')