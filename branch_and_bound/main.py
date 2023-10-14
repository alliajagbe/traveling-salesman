import numpy as np

from distance import calculate_distance_matrix
from branch_bound import tsp_branch_and_bound 


def file_reader(file):
    with open(file) as f:
        problem_type = f.readline().strip()
        n = int(f.readline().strip())

        if problem_type == 'EUCLIDEAN':
            coordinates = [tuple(map(float, f.readline().strip().split())) for _ in range(n)]
            print("Coordinates: ", coordinates)
            distance_matrix = calculate_distance_matrix(coordinates)
        elif problem_type == 'NON-EUCLIDEAN':
            distance_matrix = np.array([list(map(float, line.split())) for line in f.readlines()])

        return distance_matrix
    
distance_matrix = file_reader('input.txt')

tour, tour_length = tsp_branch_and_bound(distance_matrix)
print("Shortest TSP tour:", tour)
print("Tour length:", tour_length)