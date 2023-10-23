import random
import time
from itertools import chain

def read_input(file_path):
    with open(file_path, 'r') as file:
        tsp_type = file.readline().strip()
        N = int(file.readline())
        cities = [tuple(map(float, file.readline().split())) for _ in range(N)]
        distances = [list(map(float, file.readline().split())) for _ in range(N)]
        return tsp_type, N, cities, distances

def calculate_tour_length(tour, distances):
    total_length = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    total_length += distances[tour[-1]][tour[0]]  # Return to the starting city
    return total_length

def pmx_crossover(parent1, parent2):
    n = len(parent1)
    start, end = sorted(random.sample(range(n), 2))
    child = [-1] * n
    mapping = {}

    # Copy the segment from parent1 to the child
    child[start:end] = parent1[start:end]

    # Map the corresponding elements in parent2 to the child
    for i in range(start, end):
        if parent2[i] not in child:
            current = parent2[i]
            j = parent2.index(parent1[i])

            while child[j] != -1:
                j = parent2.index(parent1[j])

            child[j] = current

    # Copy the remaining elements from parent2
    for i in range(n):
        if child[i] == -1:
            child[i] = parent2[i]

    return child

def tournament_selection(population, tournament_size):
    # Randomly select 'tournament_size' individuals from the population
    tournament = random.sample(population, tournament_size)

    # Find the best individual in the tournament based on tour length
    best_individual = min(tournament, key=lambda individual: calculate_tour_length(individual, distances))

    return best_individual

def ox_crossover(parent1, parent2):
    n = len(parent1)
    start, end = sorted(random.sample(range(n), 2))
    child = [-1] * n

    # Copy the segment from parent1 to the child
    child[start:end] = parent1[start:end]

    # Initialize indices for parent2
    index = end

    # Fill the remaining positions using parent2
    for i in chain(range(end, n), range(0, end)):
        if parent2[i] not in child:
            child[index] = parent2[i]
            index = (index + 1) % n

    return child


def hybrid_crossover(parent1, parent2, generation):
    if generation % 2 == 0:
        return pmx_crossover(parent1, parent2)
    else:
        return ox_crossover(parent1, parent2)

def mutate(tour):
    i, j = sorted(random.sample(range(len(tour)), 2))
    tour[i:j] = reversed(tour[i:j])

def genetic_algorithm(N, cities, distances, population_size=200, num_generations=1000, tournament_size=10):
    population = [list(range(N)) for _ in range(population_size)]
    best_tour = min(population, key=lambda tour: calculate_tour_length(tour, distances))
    best_length = calculate_tour_length(best_tour, distances)
    print(f"Generation 0: Best Tour Length = {best_length}")

    for generation in range(1, num_generations):
        new_population = [best_tour]

        while len(new_population) < population_size:
            parent1 = tournament_selection(population, tournament_size)
            parent2 = tournament_selection(population, tournament_size)
            
            child = hybrid_crossover(parent1, parent2, generation)
            mutate(child)
            new_population.append(child)

        population = new_population
        best_tour = min(population, key=lambda tour: calculate_tour_length(tour, distances))
        best_length = calculate_tour_length(best_tour, distances)
        print(f"Generation {generation}: Best Tour Length = {best_length}")

    return best_tour

def two_opt(tour, distances):
    n = len(tour)
    best_tour = tour
    improved = True

    while improved:
        improved = False
        for i in range(1, n - 2):
            for j in range(i + 1, n):
                if j - i == 1:
                    continue  # No point swapping adjacent cities
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_length = calculate_tour_length(new_tour, distances)
                if new_length < calculate_tour_length(best_tour, distances):
                    best_tour = new_tour
                    print("New tour found:", best_tour, "with cost:", new_length)
                    improved = True
        tour = best_tour

    return best_tour

if __name__ == '__main__':
    input_file = "st70.txt"
    tsp_type, N, cities, distances = read_input(input_file)

    start_time = time.time()
    tour = genetic_algorithm(N, cities, distances)
    ga_time = time.time() - start_time
    print("Time taken for Genetic Algorithm:", ga_time)
    print("Genetic Algorithm Tour:", tour)
    tour_length = calculate_tour_length(tour, distances)
    print("Total Tour Length with Genetic Algorithm:", tour_length)

    start_time = time.time()
    tour = two_opt(tour, distances)
    two_opt_time = time.time() - start_time
    print("Time taken for 2-opt:", two_opt_time)
    print("2-opt Tour:", tour)
    tour_length = calculate_tour_length(tour, distances)
    print("Total Tour Length with 2-opt:", tour_length)