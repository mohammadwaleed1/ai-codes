class GoalBasedAgent:
    def __init__(self):
        # This is the DESIRED state of the world
        self.goal = 'Clean' 

    def act(self, percept):
        # CHECK: Does the current world match my goal?
        if percept == self.goal:
            return 'Stay Idle' # Goal is already met!
        else:
            # Action taken specifically to ACHIEVE the goal
            return 'Clean the room'

class Environment:
    def __init__(self, state='Dirty'):
        self.state = state
        
    def get_percept(self):
        return self.state
        
    def clean_room(self):
        print("...Environment: Room state updated to Clean...")
        self.state = 'Clean'

def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)
        
        print(f"Step {step + 1}: Percept - {percept} | Action - {action}")
        
        if action == 'Clean the room':
            environment.clean_room()
        print("-" * 30)

# Create and Run
agent = GoalBasedAgent()
environment = Environment('Dirty')
run_agent(agent, environment, 5)