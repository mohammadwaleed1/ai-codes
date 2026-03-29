class Environment:
    def __init__(self, rain, windows_open):
        self.rain = rain
        self.windows_open = windows_open

    def get_percept(self):  
        return {'rain': self.rain, 'windows_open': self.windows_open}

    def close_windows(self):
        self.windows_open = 'Closed'

class utility:
    def __init__(self):
        self.utility_map = {
            ('Yes', 'Open'): -100,  # Raining + Window Open = Disaster
            ('Yes', 'Closed'): 10,   # Raining + Window Closed = Safe
            ('No', 'Open'): 20,     # No Rain + Window Open = Fresh Air
            ('No', 'Closed'): 5      # No Rain + Window Closed = Neutral
        }
    def updateutility(self,percept):
        states= (percept['rain'],percept['windows_open'])
        return self.utility_map[states]
    
    def act(self, percept):
        if percept['rain']=="Yes" and percept['windows_open']=="Open":
           return 'close window'
        return 'No action'


def run_agent(agent, environment, steps):
    total_utility=0
    for step in range(steps):
        percept = environment.get_percept()
        current_utility = agent.updateutility(percept)
        total_utility += current_utility
        action = agent.act(percept)
        
        print(f"Step {step + 1}: Percept: {percept} | Action: {action}")

        if action == 'close window':
            environment.close_windows()
    print(total_utility)

# --- EXECUTION ---
agent = utility()
env = Environment(rain='No', windows_open='Open')

# 2. Run for 2 steps while it's sunny
print("STARTING SIMULATION (DRY WEATHER)")
run_agent(agent, env, 2)

# 3. Change the environment (It starts raining!)
print("\n!!! WEATHER UPDATE: IT IS NOW RAINING !!!\n")
env.rain = 'Yes'

# 4. Run for 2 more steps to see the agent react
run_agent(agent, env, 2)