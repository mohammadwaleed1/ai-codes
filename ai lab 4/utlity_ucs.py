class env:
    def __init__(self,graph):
        self.graph=graph
    def get_percept(self,node):
        return self.graph(node,[])
        
class UtilityAgent:
    def __init__(self, utility_map):
        self.utility_map = utility_map   # ← utility not goal

    def get_utility(self, node):
        return self.utility_map.get(node, 0)
    

    def ucs(self,graph, start,env):
        best_node    = None
        best_utility = -1

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
            utility=self.get_utility(current_node)

            print(f"Visiting: {current_node} | Cost: {current_cost} | Utility: {utility}")
            if utility > best_utility:
                best_utility = utility
                best_node    = current_node

            # explore neighbors
            for neighbor, cost in env.get_percept(current_node):
                new_cost = current_cost + cost

                # only add if cheaper path found
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = current_node
                    frontier.append([new_cost, neighbor])
        # goal found — trace path back
    
        path = []
        node = best_node
        while node is not None:
            path.append(node)
            node = came_from[node]
        path.reverse()
        print(f"Path Found  : {path}")
        print(f"Total Cost  : {current_cost}")


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
utility_map = {
    'A': 0,
    'B': 10,
    'C': 20,
    'D': 30,
    'E': 15,
    'F': 25,
    'G': 40,
    'H': 50,
    'I': 100
}
env   = env(graph)
agent = UtilityAgent(utility_map)
agent.ucs(env, 'A')