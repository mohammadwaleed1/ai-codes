class Environment:
    def __init__(self, initial_state='Dirty'):
        self.state = initial_state

    def get_percept(self):
        return self.state

    def apply_action(self, action):
            self.state = 'Clean'

class UtilityBasedAgent:
    def __init__(self):
        self.utility_map = {'Dirty': -10, 'Clean': 10}
        
    def evaluate_utility(self, percept):
        return self.utility_map[percept]

    def act(self, percept):
        if percept == 'Dirty':
          
            return 'Clean'
        else:
            return 'No Action'

def run_simulation(agent, env, steps):
    total_utility = 0
    for i in range(1, steps + 1):
        percept = env.get_percept()
        
        # 1. Evaluate current happiness 
        current_utility = agent.evaluate_utility(percept)
        total_utility += current_utility
        
        # 2. Select the best action based on utility logic
        chosen_action = agent.act(percept)
        print(f"Step {i}: State: {percept} | Action: {chosen_action} | Utility: {current_utility}")
        
        if chosen_action == 'Clean':
            env.apply_action(chosen_action)

    print("-" * 30)
    print(f"Final Total Utility: {total_utility}")

# --- Run it ---
my_agent = UtilityBasedAgent()
my_env = Environment()
run_simulation(my_agent, my_env, 5)