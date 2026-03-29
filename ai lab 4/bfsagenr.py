# Environment Class
class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return self.graph.get(node, [])


# Agent Class
class Agent:
    def __init__(self, goal):
        self.goal = goal

    def bfs_search(self, env, start):
        visited = []
        queue = [start]

        while queue:
            node = queue.pop(0)
            

            if node not in visited:
                print("Agent visiting:", node)
                visited.append(node)

                if node == self.goal:
                    return visited

                children = env.get_percept(node)
                for child in children:
                    if child not in visited:
                        queue.append(child)

        return "Goal Not Found"


def simulate(environment, agent, start):
    print("Simulation Started")
    result = agent.bfs_search(environment, start)
    print("Simulation Ended")
    print("Result:", result)

 
# Tree Representation
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

# Create objects
env = Environment(tree)
agent = Agent('F')

# Run Simulation
simulate(env, agent, 'A')
