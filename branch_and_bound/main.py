# Read input
problem_type = input()
n = int(input())
coordinates = []

# Read coordinates
for _ in range(n):
    x, y = map(float, input().split())
    coordinates.append((x, y))

# Calculate the distance matrix
distance_matrix = calculate_distance_matrix(coordinates)

# Example usage:
tour, tour_length = tsp_branch_and_bound(distance_matrix)
print("Shortest TSP tour:", tour)
print("Tour length:", tour_length)