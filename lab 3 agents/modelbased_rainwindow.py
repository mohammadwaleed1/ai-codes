class Environment:
    def __init__(self, rain='No', windows_open='Open'):
        self.rain = rain
        self.windows_open = windows_open

    def get_percept(self):
        """Returns the current state of the world."""
        return {'rain': self.rain, 'windows_open': self.windows_open}

    def close_windows(self):
        """Updates the physical state of the windows."""
        self.windows_open = 'Closed'

class ModelBasedAgent:
    def __init__(self):
        # Initial internal 'memory' or 'model' of the world
        self.model = {}
    def update_model(self,percept):
        model=percept
    
    def act(self, percept):
        """Updates internal memory and then decides on an action."""
        # 1. Update the internal model with new information
        self.model.update(percept)
        
        # 2. Logic based on the updated model
        if self.model['rain'] == 'Yes' and self.model['windows_open'] == 'Open':
            return 'Close the windows'
        else:
            return 'No action needed'

def run_agent(agent, environment, steps):
    for step in range(steps):
        # The agent 'perceives' the environment
        percept = environment.get_percept()
        
        # The agent 'thinks' and decides
        action = agent.act(percept)
        
        print(f"Step {step + 1}: Percept: {percept} | Action: {action}")

        # The world changes only if the agent takes an action
        if action == 'Close the windows':
            environment.close_windows()
        print("-" * 40)

# --- EXECUTION ---

# 1. Setup
agent = ModelBasedAgent()
env = Environment(rain='No', windows_open='Open')

# 2. Run for 2 steps while it's sunny
print("STARTING SIMULATION (DRY WEATHER)")
run_agent(agent, env, 2)

# 3. Change the environment (It starts raining!)
print("\n!!! WEATHER UPDATE: IT IS NOW RAINING !!!\n")
env.rain = 'Yes'

# 4. Run for 2 more steps to see the agent react
run_agent(agent, env, 2)