from queue import PriorityQueue

# 1. Define the Graph based on your image
# Each node points to a list of (Neighbor, Heuristic_Value)
graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'D': [], 'E': [], 'F': [], 'G': [], 'I': [], 'J': []
}

def best_first_search(graph, start, goal):
    visited = set()
    pq = PriorityQueue()
    came_from={start:None}
    # PriorityQueue stores tuples: (priority, node)
    # The 'priority' here is the Heuristic (green numbers)
    pq.put((0, start)) 

    while not pq.empty():
        # cost = heuristic value, node = node name
        cost, node = pq.get()

        if node not in visited:
            visited.add(node)

            if node == goal:
                path=[]
                node=goal
                while node is not None:
                    path.append(node)
                    node=came_from[node]
                print("\nGoal reached!")
                path.reverse()
                print(f"Path Found  : {path}")
                return True

            # Explore neighbors and put their weights (heuristics) into PQ
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    pq.put((weight, neighbor))
                    came_from[neighbor]=node

    print("\nGoal not reachable!")
    return False

# Run Simulation
print("Best-First Search Path:")
best_first_search(graph, 'S', 'I')