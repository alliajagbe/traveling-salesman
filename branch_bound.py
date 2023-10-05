from itertools import permutations
from distance import calculate_tour_distance
from input_reader import read_euclidean_input
from distance import calculate_euclidean

def tsp_branch_and_bound(distance_matrix):
    num_cities = len(distance_matrix)
    min_tour = None
    min_distance = float('inf')

    def bound(path, distance_matrix):
        # Calculate lower bound using Minimum Spanning Tree (MST) heuristic
        unvisited_cities = set(range(num_cities)) - set(path)
        if len(unvisited_cities) == 0:
            return calculate_tour_distance(path, distance_matrix)
        
        min_dist_to_unvisited = min(
            distance_matrix[i][j]
            for i in path
            for j in unvisited_cities
        )
        mst_bound = sum(
            min(distance_matrix[i][j] for j in unvisited_cities)
            for i in path
        ) + min_dist_to_unvisited * len(unvisited_cities)
        
        return mst_bound

    def tsp_recursive(path, distance, bound_estimate):
        nonlocal min_tour, min_distance

        if len(path) == num_cities:
            distance += distance_matrix[path[-1]][path[0]]  # Return to the starting city
            if distance < min_distance:
                min_distance = distance
                min_tour = path.copy()
            return

        for city in range(num_cities):
            if city not in path:
                new_path = path + [city]
                new_distance = distance + distance_matrix[path[-1]][city]

                if new_distance + bound(new_path, distance_matrix) < min_distance:
                    tsp_recursive(new_path, new_distance, bound_estimate)

    for start_city in range(num_cities):
        tsp_recursive([start_city], 0, bound([] , distance_matrix))

    return min_tour, min_distance

def main():
    input_type = input().strip()
    
    if input_type == "EUCLIDEAN":
        cities = read_euclidean_input()
        num_cities = len(cities)
        distance_matrix = np.zeros((num_cities, num_cities))
        
        # Calculate distances for the Euclidean case
        for i in range(num_cities):
            for j in range(i+1, num_cities):
                distance_matrix[i][j] = calculate_euclidean(cities[i], cities[j])
                distance_matrix[j][i] = distance_matrix[i][j]
    else:
        print("Invalid input type. Please use EUCLIDEAN.")
        return

    min_tour, min_distance = tsp_branch_and_bound(distance_matrix)
    
    print("Shortest TSP Tour:", min_tour)
    print("Total Distance:", min_distance)

if __name__ == "__main__":
    main()



