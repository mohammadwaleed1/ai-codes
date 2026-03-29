from queue import PriorityQueue

graph = {
    'S': {'A': 3, 'B': 6, 'C': 5},
    'A': {'D': 9, 'E': 8},
    'B': {'F': 12, 'G': 14},
    'C': {'H': 7},
    'H': {'I': 5, 'J': 6},
    'I': {'K': 1, 'L': 10, 'M': 2},
    'D': {}, 'E': {},
    'F': {}, 'G': {},
    'J': {}, 'K': {},
    'L': {}, 'M': {}
}
def hill_climbing(start, goal):

    current = (0, [start])        # ← same as beam = [(0,[start])]
    unvisited = PriorityQueue()
    visited = []

    while True:

        current_cost, current_path = current    # unpack
        current_node = current_path[-1]

        if current_node == goal:
            print(f"Path Found : {' → '.join(current_path)}")
            print(f"Total Cost : {current_cost}")
            return

        visited.append(current_node)
        neighbors = graph.get(current_node, {})

        if neighbors:
            sorted_neighbors = sorted(neighbors.items(), key=lambda x: x[1])
            best_neighbor, best_cost = sorted_neighbors[0]

            for neighbor, cost in sorted_neighbors[1:]:
                if neighbor not in visited:
                    unvisited.put((current_cost + cost, current_path + [neighbor]))

            # update current — same tuple style
            current = (current_cost + best_cost, current_path + [best_neighbor])

        else:
            print(f"Dead end at {current_node}!")

            if unvisited.empty():
                print("Goal not found")
                return

            current = unvisited.get()   # ← returns (cost, path) tuple directly ✅
            print(f"Backtracking to : {current[1][-1]}")