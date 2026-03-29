import random
from collections import namedtuple
# Define what a "Thing" is
Thing = namedtuple('Thing', ['name', 'value', 'weight'])

# Create a list of 'things'
things = [
    Thing('Laptop', 500, 2),
    Thing('Headphones', 150, 1),
    Thing('Gold Bar', 1000, 5),
    Thing('Water Bottle', 10, 1)
]
# 1. Your Genome function
def generate_genome(length):
    genome = []
    for i in range(length):
        # Pick either 0 or 1 randomly
        bit = random.randint(0, 1)
        genome.append(bit)
    return genome

# 2. Your Population function
def generate_population(size, genome_length):
    population = []
    
    # The loop runs 'size' times!
    for i in range(size):
        # Generate one genome
        individual = generate_genome(genome_length)
        # Add it to the population list
        population.append(individual)
        
    return population
def calculate_fitness(genome, things, weight_limit):
    total_weight = 0
    total_value = 0
    
    # Loop through every item and check if our genome picked it
    for i in range(len(things)):
        if genome[i] == 1:
            # Add the weight and value of the 'i-th' thing
            total_weight += things[i].weight
            total_value += things[i].value
            
        # Check if we broke the rule (Bag too heavy!)
        if total_weight > weight_limit:
            return 0  # Disqualified! Fitness is zero.

    # If we finish the loop and weight is okay, return the value
    return total_value


def selection_function(population, things, weight_limit):
    # --- Step 1: Find Parent A ---
    # Pick two random people from the crowd
    candidate1 = random.choice(population)
    candidate2 = random.choice(population)
    
    # Calculate their fitness scores
    score1 = calculate_fitness(candidate1, things, weight_limit)
    score2 = calculate_fitness(candidate2, things, weight_limit)
    
    # The one with the higher score is Parent A
    if score1 > score2:
        parent_a = candidate1
    else:
        parent_a = candidate2
        
    # --- Step 2: Find Parent B ---
    # Pick two MORE random people
    candidate3 = random.choice(population)
    candidate4 = random.choice(population)
    
    score3 = calculate_fitness(candidate3, things, weight_limit)
    score4 = calculate_fitness(candidate4, things, weight_limit)
    
    # The winner is Parent B
    if score3 > score4:
        parent_b = candidate3
    else:
        parent_b = candidate4
        
    # Return both parents as a pair
    return parent_a, parent_b
def crossover(genome_a, genome_b, p):
    # Guard 1: Make sure they are the same size
    if len(genome_a) != len(genome_b):
        # Instead of 'return', return the originals so the loop doesn't break
        return genome_a, genome_b 
    
    # Guard 2: Make sure there is enough DNA to actually cut
    if len(genome_a) >= 2:
        child_a = genome_a[0:p] + genome_b[p:]
        child_b = genome_b[0:p] + genome_a[p:]
        return child_a, child_b
    
    # Fallback: If genome is only 1 item long, just return the parents
    return genome_a, genome_b

def mutation(genome, a):
    # Create a brand new copy so we don't break the original
    mutated_genome = genome.copy()
    
    if mutated_genome[a] == 1:
        mutated_genome[a] = 0
    else:
        mutated_genome[a] = 1
        
    return mutated_genome

def population_fitness(population,thing,weigh_limit):
    for a in population:
        score=calculate_fitness(a,thing,weigh_limit)
        print(f"Genome {a} has a fitness of: {score}")
        total+=score
        return score
    




def run_evolution(things, weight_limit, population_size, generation_limit=50):
    # 1. Start: Create the first group
    population = generate_population(population_size, len(things))
    
    for i in range(generation_limit):
        # 2. Score and Sort (No lambda!)
        # We create a list of (score, genome) pairs
        scored_population = []
        for genome in population:
            score = calculate_fitness(genome, things, weight_limit)
            scored_population.append((score, genome))
        
        # Sort them (highest score at the top)
        scored_population.sort(reverse=True)
        
        # Pull the genomes back out into a sorted list
        population = []
        for pair in scored_population:
            population.append(pair[1])

        # 3. Print Stats for this generation
        best_score = calculate_fitness(population[0], things, weight_limit)
        print(f"Gen {i} | Best Score: {best_score}")

        # 4. Elitism: Keep the best 2 survivors exactly as they are
        next_gen = [population[0], population[1]]

        # 5. Breeding: Fill the rest of the population
        while len(next_gen) < population_size:
            # Selection
            parent_a, parent_b = selection_function(population, things, weight_limit)
            
            # Crossover (using p=2 as your cut point)
            child_a, child_b = crossover(parent_a, parent_b, 2)
            
            # Mutation (flip a random index 'a')
            child_a = mutation(child_a, random.randint(0, len(things) - 1))
            child_b = mutation(child_b, random.randint(0, len(things) - 1))
            
            next_gen.append(child_a)
            if len(next_gen) < population_size:
                next_gen.append(child_b)

        # 6. Update the population for the next loop
        population = next_gen

    # Return the ultimate winner from the final generation
    return population[0]