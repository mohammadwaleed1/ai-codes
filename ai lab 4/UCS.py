def ucs(graph, start, goal):

    # frontier stores [cost, node]
    frontier = [[0, start]]
    
    # visited so we don't revisit
    visited = []
    
    # track path — who did we come from
    came_from = {start: None}
    
    # track cost to reach each node
    cost_so_far = {start: 0}

    while frontier:

        # sort by cost — lowest cost first
        frontier.sort()
        
        # pick lowest cost node
        current_cost, current_node = frontier.pop(0)

        # skip if already visited
        if current_node in visited:
            continue

        # mark as visited
        visited.append(current_node)

        # goal found — trace path back
        if current_node == goal:
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            print(f"Path Found  : {path}")
            print(f"Total Cost  : {current_cost}")
            return

        # explore neighbors
        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost

            # only add if cheaper path found
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current_node
                frontier.append([new_cost, neighbor])

    print("Goal not found")


# --- graph ---
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {'G': 1},
    'E': {'H': 2},
    'F': {'I': 1},
    'G': {'I': 3},
    'H': {'I': 2},
    'I': {}
}

ucs(graph, 'A', 'I')