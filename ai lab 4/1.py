def tsp(graph, start):

    # frontier stores [cost, current_node, path]
    frontier = [[0, start, [start]]]

    best_cost = float('inf')
    best_path = None

    all_nodes = set(graph.keys())

    while frontier:

        # sort by cost — lowest first
        frontier.sort()

        # pick lowest cost
        current_cost, current_node, path = frontier.pop(0)

        # prune — skip if already worse than best
        if current_cost >= best_cost:
            continue

        # all nodes visited — try return to start
        if set(path) == all_nodes:
            if start in graph[current_node]:
                total_cost = current_cost + graph[current_node][start]
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_path = path + [start]
            continue

        # explore neighbors not yet in path
        for neighbor, cost in graph[current_node].items():
            if neighbor not in path:
                new_cost = current_cost + cost
                new_path = path + [neighbor]
                frontier.append([new_cost, neighbor, new_path])

    if best_path:
        print(f"Best Path  : {' → '.join(best_path)}")
        print(f"Total Cost : {best_cost}")
    else:
        print("No complete tour found")


graph = {
    '1': {'2': 10, '4': 20, '3': 15},
    '2': {'4': 25, '1': 10, '3': 35},
    '3': {'2': 35, '4': 30, '1': 15},
    '4': {'2': 25, '3': 30, '1': 20},
}

tsp(graph, '1')
