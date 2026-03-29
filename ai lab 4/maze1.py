#IDS
maze = [
    ['S',0,0,1,0],
    [1,0,1,0,0],
    [0,0,0,0,'G'],
    [1,1,0,1,1]
]

def dls_maze(maze,start,goal,limit):
    stack = [(start,0)]  
    visited = set()

    while stack:
        (r,c), depth = stack.pop()
        if depth > limit:
            continue  
        if (r,c) in visited:
            continue
        visited.add((r,c))

        print(f"Visiting: {(r,c)}, Depth: {depth}")

        if maze[r][c] == goal:
            return maze[r][c]

        for cr,cc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr,nc = r+cr, c+cc
            if 0<=nr<len(maze) and 0<=nc<len(maze[0]):
                if maze[nr][nc] != 1 and (nr,nc) not in visited:
                    stack.append(((nr,nc), depth+1))
    return None

def IDS(maze, start, goal, limit):
    for depth in range(limit + 1):
        print(f"\nIDS iteration with depth limit {depth}")
        result = dls_maze(maze, start, goal, depth)
        if result:
            print(f"\nGoal '{goal}' found at depth {depth}")
            return result
    print("goal not found")

start = (0, 0) 
goal = 'G'
depth_limit = 6 # number of moves acting as dept limit
IDS(maze, start, goal, depth_limit)




