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
    for i in range(n - 1):
        total_length += distances[tour[i]][tour[i + 1]]
    total_length += distances[tour[-1]][tour[0]]  # Return to the starting city
    return total_length

def simulated_annealing(N, cities, distances, initial_temperature=1000, cooling_rate=0.995, max_iterations=1000):
    current_tour = list(range(N))
    current_length = calculate_tour_length(current_tour, distances)

    best_tour = current_tour
    best_length = current_length

    temperature = initial_temperature

    for iteration in range(max_iterations):
        if temperature <= 0.1:
            break

        # Generate a random neighboring tour by swapping two cities
        i, j = random.sample(range(N), 2)
        new_tour = current_tour[:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]

        new_length = calculate_tour_length(new_tour, distances)

        # Calculate the change in tour length
        delta_length = new_length - current_length

        # If the new tour is shorter or accepted probabilistically, update the tour
        if delta_length < 0 or random.random() < math.exp(-delta_length / temperature):
            current_tour = new_tour
            current_length = new_length

            # Update the best tour if needed
            if current_length < best_length:
                best_tour = current_tour
                best_length = current_length
                print("New tour found:", best_tour)

        # Cool down the temperature
        temperature *= cooling_rate

    return best_tour

if __name__ == '__main__':
    input_file = "input.txt"
    tsp_type, N, cities, distances = read_input(input_file)
    print(tsp_type)
    print(N)
    print(cities)
    print(distances)

    # Apply the Simulated Annealing Algorithm to approximate the TSP
    tour = simulated_annealing(N, cities, distances)

    # Calculate the final tour length
    tour_length = calculate_tour_length(tour, distances)

    for city_index in tour:
        print(cities[city_index])
    print("Total Tour Length:", tour_length)
