import sys
import random
import math

def read_input(file_path):
    with open(file_path, 'r') as file:
        tsp_type = file.readline().strip()
        N = int(file.readline())
        cities = []
        for _ in range(N):
            x, y = map(float, file.readline().split())
            cities.append((x, y))
        distances = []
        for _ in range(N):
            distances.append(list(map(float, file.readline().split())))
        return tsp_type, N, cities, distances

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_tour_length(tour, distances):
    total_length = 0.0
    n = len(tour)
    for i in range(n):
        total_length += distances[tour[i]][tour[(i + 1) % n]]
    return total_length

def generate_initial_population(N, population_size):
    population = []
    for _ in range(population_size):
        tour = list(range(N))
        random.shuffle(tour)
        population.append(tour)
    return population

def partially_mapped_crossover(parent1, parent2):
    n = len(parent1)
    start, end = sorted(random.sample(range(n), 2))

    child = [-1] * n
    child[start:end] = parent1[start:end]

    for i in range(n):
        if start <= i < end:
            continue
        gene = parent2[i]
        while gene in child:
            index = parent2.index(gene)
            gene = parent1[index]
        child[i] = gene

    return child

def swap_mutation(tour, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]

def tournament_selection(population, fitness, tournament_size):
    tournament = random.sample(range(len(population)), tournament_size)
    best_index = min(tournament, key=lambda i: fitness[i])
    return population[best_index]

def genetic_algorithm(N, cities, distances, population_size=100, generations=1000, mutation_rate=0.01, tournament_size=5):
    population = generate_initial_population(N, population_size)
    best_tour = None
    best_tour_length = float('inf')

    for generation in range(generations):
        # Evaluate fitness of the population
        fitness = [1.0 / calculate_tour_length(tour, distances) for tour in population]

        new_population = []

        while len(new_population) < population_size:
            # Select parents using tournament selection
            parent1 = tournament_selection(population, fitness, tournament_size)
            parent2 = tournament_selection(population, fitness, tournament_size)

            # Create children through crossover (Partially Mapped Crossover)
            child1 = partially_mapped_crossover(parent1, parent2)
            child2 = partially_mapped_crossover(parent2, parent1)

            # Apply mutation to the children (Swap Mutation)
            swap_mutation(child1, mutation_rate)
            swap_mutation(child2, mutation_rate)

            new_population.extend([child1, child2])

        population = new_population

        # Find the best tour in the current generation
        current_best_tour = min(population, key=lambda tour: calculate_tour_length(tour, distances))
        current_best_tour_length = calculate_tour_length(current_best_tour, distances)

        # Check if the current tour is better than the previous best tour
        if current_best_tour_length < best_tour_length:
            best_tour = current_best_tour
            best_tour_length = current_best_tour_length

            # Print the best tour in this generation
            print(f"Generation {generation + 1}:")
            for city_index in best_tour:
                print(cities[city_index])
            print("Total Tour Length:", best_tour_length)
            print("")

    return best_tour

if __name__ == '__main__':
    input_file = "input.txt"
    tsp_type, N, cities, distances = read_input(input_file)

    best_tour = genetic_algorithm(N, cities, distances)

    tour_length = calculate_tour_length(best_tour, distances)

    for city_index in best_tour:
        print(cities[city_index])
    print("Total Tour Length:", tour_length, file=sys.stderr)
