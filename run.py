from input_reader import read_euclidean_input, read_non_euclidean_input
from distance import calculate_euclidean, calculate_tour_distance
from nearest_neighbour import nearest_neighbor
import numpy as np

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
        
        # Display coordinates
        print("Coordinates of Cities:")
        for i, city in enumerate(cities):
            print(f"City {i}: {city}")
    elif input_type == "NON-EUCLIDEAN":
        distance_matrix = read_non_euclidean_input()
    else:
        print("Invalid input type. Please use EUCLIDEAN or NON-EUCLIDEAN.")
        return

    best_tour = nearest_neighbor(distance_matrix)
    print("PATH REPRESENTATION OF TOUR:")
    print(" ".join(map(str, best_tour)))

if __name__ == "__main__":
    main()