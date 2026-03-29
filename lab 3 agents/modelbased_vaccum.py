class ModelBasedAgent:
    def __init__(self):
        # The 'model' allows the agent to track the state of the world
        self.model = {'state': None}

    def update_model(self, percept):
        self.model['state'] = percept
        print(f"Internal Model Updated: {self.model}")

    def predict_action(self):
        # Logic based on the internal model rather than just raw percepts
        if self.model['state'] == 'Dirty':
            return 'Suck'
        else:
            return 'NoOp (Nothing to do)'

    def act(self, percept):
        self.update_model(percept)
        return self.predict_action()

class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'

def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)
        
        print(f"Step {step + 1}: Percept - {percept}, Action - {action}")
        
        # Environmental reaction to the agent's action
        if action == 'Suck':
            environment.clean_room()
        print("-" * 30)

# Execution
agent = ModelBasedAgent()
environment = Environment()
run_agent(agent, environment, 5)