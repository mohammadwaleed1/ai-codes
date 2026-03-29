from queue import PriorityQueue

# 1. Graph with Edge Costs (ignored by Greedy BFS, but kept for structure)
maze = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 0, 0]
]

start = (0, 0)
goal  = (4, 4)

def get_neighbours(maze,node):
    row,col=node
    neighbour=[]
    rl=len(maze)
    rc=len(maze[0])
    
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    for i,j in moves:
        new_row=row+i
        new_col=col+j
        if 0<=new_row<rl and 0<=new_col<rc:
            if maze[new_row][new_col]==0:
                neighbour.append((new_col,new_row))
    return neighbour

def manhattan(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1-x2) + abs(y1-y2)


def a_star_search(maze, start, goal):
    visited = set()
    pq = PriorityQueue()
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
            for neighbor in get_neighbours(maze,node):
                if neighbor not in visited:
                    h=manhattan(neighbor,goal)
                    # g = path cost from start to parent + cost of this new edge
                    new_g = g_val + 1
                    # f = g + neighbor's heuristic
                    
                    new_f = new_g + h
                    
                    pq.put((new_f, new_g, neighbor))

    print("\nGoal not reachable!")
    return False

print("A* Search Path:")
a_star_search(maze,start,goal)
