import random
import math
import time

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

def calculate_tour_length(tour, distances):
    total_length = 0.0
    n = len(tour)
    for i in range(n - 1):
        total_length += distances[tour[i]][tour[i + 1]]
    total_length += distances[tour[-1]][tour[0]]  # Return to the starting city
    return total_length

def partially_mapped_crossover(parent1, parent2):
    n = len(parent1)
    cut_points = sorted(random.sample(range(n), 2))
    child = [-1] * n
    mapping = {}
    
    for i in range(cut_points[0], cut_points[1]):
        child[i] = parent1[i]
        mapping[parent2[i]] = parent1[i]
    
    for i in range(n):
        if cut_points[0] <= i < cut_points[1]:
            continue  # The middle section is already filled
        current = parent2[i]
        while current in mapping:
            current = parent1[parent2.index(current)]
        child[i] = current
    
    return child

def mutate(tour):
    i, j = sorted(random.sample(range(len(tour)), 2))
    tour[i:j] = reversed(tour[i:j])

def genetic_algorithm(N, cities, distances, population_size=100, num_generations=1000):
    population = [list(range(N)) for _ in range(population_size)]
    
    for generation in range(num_generations):
        population = sorted(population, key=lambda tour: calculate_tour_length(tour, distances))
        best_tour = population[0]
        best_length = calculate_tour_length(best_tour, distances)
        print(f"Generation {generation}: Best Tour Length = {best_length}")
        
        new_population = [best_tour]
        
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population, 2)
            child = partially_mapped_crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        
        population = new_population

    return best_tour

if __name__ == '__main__':
    input_file = "200.txt"
    tsp_type, N, cities, distances = read_input(input_file)

    start_time = time.time()
    tour = genetic_algorithm(N, cities, distances)
    ga_time = time.time() - start_time
    print("Time taken for Genetic Algorithm:", ga_time)
    print("Genetic Algorithm Tour:", tour)
    tour_length = calculate_tour_length(tour, distances)
    print("Total Tour Length with Genetic Algorithm:", tour_length)

