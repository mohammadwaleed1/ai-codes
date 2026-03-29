import random

class SimpleLearningAgent:
    def __init__(self, actions):
        self.actions = actions
        self.success_count = {}
        self.epsilon = 0.2  # 20% exploration rate

        # initialize all counts to 0
        for action in actions:
            self.success_count[action] = 0

    def act(self, percept):
        # 20% of time → explore randomly
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)  # random action
        
        # 80% of time → pick best known action
        return max(self.actions, key=lambda a: self.success_count[a])

    def learn(self, action, reward):
        # if action gave reward, increment its count
        if reward > 0:
            self.success_count[action] += 1


class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'
        return 10       # positive reward

    def no_action_reward(self):
        return 0        # no reward


def run_agent(agent, environment, steps):
    for step in range(steps):

        # step 1 - observe
        percept = environment.get_percept()

        # step 2 - act
        action = agent.act(percept)

        # step 3 - get reward
        if percept == 'Dirty':
            reward = environment.clean_room()
        else:
            reward = environment.no_action_reward()

        # step 4 - learn
        agent.learn(action, reward)

        # step 5 - print
        print(f"Step {step+1}:")
        print(f"  Percept        : {percept}")
        print(f"  Action         : {action}")
        print(f"  Reward         : {reward}")
        print(f"  Success Counts : {agent.success_count}")
        print()