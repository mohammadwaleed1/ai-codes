#task 1
from queue import PriorityQueue
graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [], 'E': [],
    'F': [], 'G': [],
    'J': [], 'K': [],
    'L': [], 'M': []
}

def multi_goal_search(start, goals):
    pq = PriorityQueue()
    pq.put((0, start, [], set())) 

    while not pq.empty():
        cost, node, path, visited_goals = pq.get()
        path = path + [node]
        if node in goals:
            visited_goals = visited_goals | {node}
        if visited_goals == set(goals):
            print("All goals reached!")
            print("Path:", path)
            print("Total Cost:", cost)
            return
        for neighbor, weight in graph[node]:
            pq.put((cost + weight, neighbor, path, visited_goals))

    print("Goals not reachable")
multi_goal_search('S', ['I', 'M'])


#task 2

import heapq
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('D', 1)],
    'C': [('G', 7)],
    'D': [('G', 3)],
    'G': []
}
h = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 1,
    'G': 0
}

def astar(start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    
    g = {node: float('inf') for node in graph}
    g[start] = 0
    parent = {}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            # Reconstruct path
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1], g[goal]

        for neighbor, cost in graph[current]:
            new_cost = g[current] + cost
            if new_cost < g[neighbor]:
                g[neighbor] = new_cost
                parent[neighbor] = current
                f = new_cost + h[neighbor]
                heapq.heappush(pq, (f, neighbor))

    return None, float('inf')
def update_edge_cost(u, v, new_cost):
    for i, (neighbor, cost) in enumerate(graph[u]):
        if neighbor == v:
            graph[u][i] = (v, new_cost)
            print(f"Edge cost updated: {u} -> {v} = {new_cost}")
            break
start = 'S'
goal = 'G'
path, cost = astar(start, goal)
print("Initial Path:", path, "Cost:", cost)
update_edge_cost('A', 'C', 10)
path, cost = astar(start, goal)
print("Updated Path:", path, "Cost:", cost)

update_edge_cost('B', 'D', 5)
path, cost = astar(start, goal)
print("Updated Path:", path, "Cost:", cost)

#task 3
delivery_points = {
    'P1': (2, 3, 1, 5),
    'P2': (5, 4, 2, 8),
    'P3': (1, 7, 3, 10),
    'P4': (6, 1, 0, 6)
}

depot = (0, 0)
current_time = 0
current_location = depot
unvisited = set(delivery_points.keys())
route = []
def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

while unvisited:
    best_point = None
    best_priority = float('inf')
    
    for point in unvisited:
        x, y, start, end = delivery_points[point]
        dist = distance(current_location, (x, y))
        arrival_time = current_time + dist
        if arrival_time > end:
            continue 
        slack = end - arrival_time
        priority = dist + slack 
        if priority < best_priority:
            best_priority = priority
            best_point = point

    if best_point is None:
        print("Cannot deliver to remaining points within time windows!")
        break
    x, y, start, end = delivery_points[best_point]
    travel_time = distance(current_location, (x, y))
    arrival_time = current_time + travel_time

    current_time = max(arrival_time, start)
    route.append(best_point)
    current_location = (x, y)
    unvisited.remove(best_point)

print("Delivery route:", route)
print("Total time:", current_time)
