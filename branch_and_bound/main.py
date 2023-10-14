from distance import calculate_distance_matrix
from branch_bound import tsp_branch_and_bound 

# Read input
problem_type = input("EUCLIDEAN or NON-EUCLIDEAN: ").strip()
n = int(input("Enter Number of Cities: "))
coordinates = []

# Read coordinates
for i in range(n):
    x, y = map(float, input(f"Enter the Coordinates for City {i}:").split())
    coordinates.append((x, y))

# Calculate the distance matrix
distance_matrix = calculate_distance_matrix(coordinates)
print("Distance Matrix: ")
print(distance_matrix)

# Example usage:
tour, tour_length = tsp_branch_and_bound(distance_matrix)
print("Shortest TSP tour:", tour)
print("Tour length:", tour_length)