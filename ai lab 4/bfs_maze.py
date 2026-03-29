
maze = [
    ['S',0,0,1,0],
    [1,0,1,0,0],
    [0,0,0,0,'G'],
    [1,1,0,1,1]
]

def bfsmaze(maze,start,goal):
    came_from={start:None}
    stack = [(start)]  
    visited = set()

    while stack:
        (r,c)= stack.pop(0)  
        if (r,c) in visited:
            continue
        visited.add((r,c))

        print((r,c),end=' -> ')

        if maze[r][c] == goal:
             print(f"\nGoal '{goal}'")
             return maze[r][c]

        for cr,cc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr,nc=r+cr, c+cc
            if 0<=nr<len(maze) and 0<=nc<len(maze[0]):
                if maze[nr][nc] != 1 and (nr,nc) not in visited:
                    stack.append(((nr,nc)))
    print("goal not found")

start = (0, 0) 
goal = 'G'
bfsmaze(maze, start, goal)

