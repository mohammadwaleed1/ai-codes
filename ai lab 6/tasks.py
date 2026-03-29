#Q1
import chess


piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0
}

def evaluate_board(board):
    score = 0
    for piece_type in piece_values:
        score += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
        score -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]
    return score


def beam_search(board, beam_width, depth):
    
    beams = [(board.copy(), [], evaluate_board(board))]

    for _ in range(depth):
        candidates = []

        for state, path, score in beams:

            for move in state.legal_moves:
                new_board = state.copy()
                new_board.push(move)

                new_score = evaluate_board(new_board)

                candidates.append(
                    (new_board, path + [move], new_score)
                )

        
        candidates.sort(key=lambda x: x[2], reverse=True)

        
        beams = candidates[:beam_width]

    best_state = beams[0]

    return best_state[1], best_state[2]


board = chess.Board()

moves, score = beam_search(board, beam_width=3, depth=2)

print("Best Move Sequence:", moves)
print("Evaluation Score:", score)

#Q2
import random
import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def total_distance(route):
    dist = 0
    for i in range(len(route)-1):
        dist += distance(route[i], route[i+1])
    dist += distance(route[-1], route[0])  
    return dist
def hill_climbing(points):

  
    current_route = points[:]
    random.shuffle(current_route)

    current_distance = total_distance(current_route)

    improved = True

    while improved:
        improved = False

        for i in range(len(points)):
            for j in range(i+1, len(points)):

                new_route = current_route[:]

                
                new_route[i], new_route[j] = new_route[j], new_route[i]

                new_distance = total_distance(new_route)

               
                if new_distance < current_distance:
                    current_route = new_route
                    current_distance = new_distance
                    improved = True

    return current_route, current_distance



points = [
    (0,0),
    (2,3),
    (5,4),
    (1,6),
    (7,2)
]

route, distance = hill_climbing(points)

print("Optimized Route:", route)
print("Total Distance:", distance)

#Q3
import random
import math

cities = [
    (0,0),
    (2,3),
    (5,4),
    (1,6),
    (7,2),
    (3,1),
    (4,7),
    (6,5),
    (8,3),
    (2,7)
]

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def total_distance(route):
    dist = 0
    for i in range(len(route)-1):
        dist += distance(route[i], route[i+1])
    dist += distance(route[-1], route[0]) 
    return dist

def fitness(route):
    return 1 / total_distance(route)

def select(population, fitnesses):
    total_fit = sum(fitnesses)
    pick = random.uniform(0, total_fit)
    current = 0
    for route, fit in zip(population, fitnesses):
        current += fit
        if current > pick:
            return route
    return population[-1]


def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[start:end] = parent1[start:end]

    pointer = 0
    for city in parent2:
        if city not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = city
    return child


def mutate(route, mutation_rate=0.1):
    route = route[:]
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]
    return route
def genetic_algorithm(cities, population_size=50, generations=200):
    
    population = [random.sample(cities, len(cities)) for _ in range(population_size)]

    best_route = population[0]
    best_distance = total_distance(best_route)

    for gen in range(generations):
        fitnesses = [fitness(route) for route in population]
        new_population = []

        for _ in range(population_size):
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

        
        for route in population:
            dist = total_distance(route)
            if dist < best_distance:
                best_distance = dist
                best_route = route

    return best_route, best_distance

best_route, best_distance = genetic_algorithm(cities)

print("Optimized Route:", best_route)
print("Total Distance:", best_distance)

#Q4
import copy

def beam_search_task_allocation(tasks, processors, beam_width=3):
    initial_state = {'assignment':[[] for _ in range(processors)], 'load':[0]*processors}
    beams = [initial_state]
    
    for task in tasks:
        candidates = []
        for state in beams:
            for p in range(processors):
                new_state = copy.deepcopy(state)
                new_state['assignment'][p].append(task['id'])
                new_state['load'][p] += task['time']
                priority_factor = sum([task['priority'] for tid in new_state['assignment'][p] 
                                       for task in tasks if task['id']==tid])
                new_state['score'] = max(new_state['load']) - 0.1*priority_factor
                candidates.append(new_state)
        candidates.sort(key=lambda x: x['score'])
        beams = candidates[:beam_width]
    
    best_state = beams[0]
    return best_state['assignment'], best_state['load']


tasks = [
    {'id': 1, 'time': 5, 'priority': 3},
    {'id': 2, 'time': 2, 'priority': 1},
    {'id': 3, 'time': 7, 'priority': 2},
    {'id': 4, 'time': 3, 'priority': 1},
    {'id': 5, 'time': 4, 'priority': 2}
]
processors = 3

allocation, load = beam_search_task_allocation(tasks, processors, beam_width=3)

print("Optimized Task Allocation:", allocation)
print("Processor Loads:", load)