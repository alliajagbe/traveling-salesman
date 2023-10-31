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
    
def read_input_from_terminal():
    tsp_type = input().strip()
    N = int(input())
    cities = []
    distances = []

    for i in range(N):
        x, y = map(float, input().split())
        cities.append((x, y))

    for i in range(N):
        row = list(map(float, input().split()))
        distances.append(row)

    return tsp_type, N, cities, distances

def calculate_tour_length(tour, distances):
    total_length = 0.0
    n = len(tour)
    for i in range(n - 1):
        total_length += distances[tour[i]][tour[i + 1]]
    total_length += distances[tour[-1]][tour[0]]  # Return to the starting city
    return total_length

def tsp_solver(N, cities, distances):

    def simulated_annealing(N, cities, distances, initial_temperature=1000.0, cooling_rate=0.99, max_iterations=100000):
        current_tour = list(range(N))
        current_length = calculate_tour_length(current_tour, distances)
        best_tour = current_tour
        best_length = current_length

        temperature = initial_temperature

        for iteration in range(max_iterations):
            new_tour = current_tour.copy()
            i, j = random.sample(range(N), 2)
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_length = calculate_tour_length(new_tour, distances)

            # Calculate the acceptance probability using the Boltzmann function
            delta_length = new_length - current_length
            exponent = -delta_length / temperature
            clipped_exponent = max(min(exponent, 709), -709) # avoiding overflow
            acceptance_probability = math.exp(clipped_exponent)

            if delta_length < 0 or random.random() < acceptance_probability: 
                current_tour = new_tour
                current_length = new_length

                if current_length < best_length:
                    best_tour = current_tour
                    best_length = current_length

            # Cooling: Linear cooling schedule
            temperature *= cooling_rate

        return best_tour

    # using 2-opt to refine the tour found by simulated annealing
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
                        printed_tour = best_tour + [best_tour[0]]
                        print(" ".join(map(str, printed_tour)))
                        improved = True
            tour = best_tour

        return best_tour
    
    tour = simulated_annealing(N, cities, distances)
    for i in range(10):
        new_tour = simulated_annealing(N, cities, distances)
        new_length = calculate_tour_length(new_tour, distances)
        if new_length < calculate_tour_length(tour, distances):
            tour = new_tour
            printed_tour = tour + [tour[0]]
            print(" ".join(map(str, printed_tour)))
    
    tour = two_opt(tour, distances)

    return tour

if __name__ == '__main__':
    
    tsp_type, N, cities, distances = read_input_from_terminal()

    tour = tsp_solver(N, cities, distances)
    printed_tour = tour + [tour[0]]
    print(" ".join(map(str, printed_tour)))
