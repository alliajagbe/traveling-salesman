import random
import math
import time
from itertools import islice, chain

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

def order_crossover(parent1, parent2):
    n = len(parent1)
    start, end = sorted(random.sample(range(n), 2))
    child = [-1] * n
    child[start:end] = parent1[start:end]

    p2 = [city for city in parent2 if city not in child]

    i = end
    while -1 in child:
        child[i] = p2.pop(0)
        i = (i + 1) % n

    return child

def mutate(tour):
    i, j = sorted(random.sample(range(len(tour)), 2))
    tour[i:j] = reversed(tour[i:j])

def genetic_algorithm(N, cities, distances, population_size=100, num_generations=1000):
    population = [list(range(N)) for _ in range(population_size)]
    best_tour = min(population, key=lambda tour: calculate_tour_length(tour, distances))
    best_length = calculate_tour_length(best_tour, distances)
    print(f"Generation 0: Best Tour Length = {best_length}")

    for generation in range(1, num_generations):
        new_population = [best_tour]

        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population, 2)
            child = order_crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)

        population = new_population
        best_tour = min(population, key=lambda tour: calculate_tour_length(tour, distances))
        best_length = calculate_tour_length(best_tour, distances)
        print(f"Generation {generation}: Best Tour Length = {best_length}")

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

