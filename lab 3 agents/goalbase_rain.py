class GoalBasedAgent:
    def __init__(self):
        # The agent's desired state of the world
        self.goal_state = {'rain': 'Yes', 'windows_open': 'Closed'}

    def act(self, percept):
        # 1. Check if it is raining
        is_raining = percept.get('rain') == 'Yes'
        window_status = percept.get('windows_open')
        
        # 2. If it's raining, check if our current state matches our goal (Closed)
        if is_raining:
            if window_status != self.goal_state['windows_open']:
                return 'Close the windows'
            else:
                return 'Goal Met: Windows are already shut'
        
        return 'No action needed: It is not raining'

class Environment:
    def __init__(self, rain='No', windows_open='Open'):
        self.rain = rain
        self.windows_open = windows_open

    def get_percept(self):
        return {'rain': self.rain, 'windows_open': self.windows_open}

    def close_windows(self):
        self.windows_open = 'Closed'

# --- Execution ---
agent = GoalBasedAgent()
env = Environment(rain='Yes', windows_open='Open')

# Step 1: Agent sees rain and open windows. Goal is NOT met.
percept = env.get_percept()
action = agent.act(percept)
print(f"Action: {action}") # Output: Close the windows

# Step 2: Environment updates
if action == 'Close the windows':
    env.close_windows()

# Step 3: Agent checks again. Goal IS met.
percept = env.get_percept()
action = agent.act(percept)
print(f"Action: {action}") # Output: Goal Met: Windows are already shut