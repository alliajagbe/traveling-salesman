import sys

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
    for i in range(len(tour) - 1):
        total_length += distances[tour[i]][tour[i+1]]
    total_length += distances[tour[-1]][tour[0]]  # Return to the starting city
    return total_length

def two_opt(tour, distances):
    n = len(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, n - 2):
            for j in range(i + 1, n):
                if j - i == 1:
                    continue  # Ignore adjacent cities
                new_tour = tour[:]
                new_tour[i:j] = tour[j - 1:i - 1:-1]  # Reverse the segment
                new_length = calculate_tour_length(new_tour, distances)
                if new_length < calculate_tour_length(tour, distances):
                    tour = new_tour
                    improved = True
                    print("Tour Length:", new_length)  # Print tour length at each step
                    for city_index in new_tour:
                        print(cities[city_index])
                    
    return tour

if __name__ == '__main__':
    input_file = "input.txt"
    tsp_type, N, cities, distances = read_input(input_file)
    print("tsp type", tsp_type)
    print("number of cities", N)
    print("cities", cities)
    print("distances", distances)

    tour = list(range(N))

    # Apply the 2-opt algorithm
    tour = two_opt(tour, distances)

    # Calculate the final tour length
    tour_length = calculate_tour_length(tour, distances)

    print("Total Tour Length:", tour_length)
